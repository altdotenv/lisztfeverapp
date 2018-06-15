from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from lisztfeverapp.users import models as user_models
from .. import db_connection as db

cursor = db.cursor

class Artist(APIView):

    def get(self, request, artist_id, format=None):

        try:
            found_artist = models.Artists.objects.get(artistid=artist_id)
        except models.Artists.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ArtistAllSerializer(found_artist)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class SearchArtist(APIView):

    def get(self, request, format=None):

        terms = request.query_params.get('terms', None)
        user = request.user

        if terms is not None:

            terms = terms.split(",")

            filter_genre = models.ArtistGenres.objects.filter(genre__in=terms)

            if filter_genre:

                terms = tuple(terms)

                cursor.execute("""
                SELECT
                  t1.artistId AS 'artist_id',
                  t1.artistName AS 'artist_name',
                  t1.imageUrl AS 'image_url',
                  t1.popularity,
                  t1.total_count,
                  t1.local_count,
                  GROUP_CONCAT(t2.genre) AS 'genres'
                FROM (
                    SELECT
                        t1.artistId,
                        t1.artistName,
                        t1.imageUrl,
                        t1.popularity,
                        COUNT(t3.eventId) AS total_count,
                        COUNT(t6.eventid) AS local_count
                    FROM (
                        SELECT
                            DISTINCT
                            t1.artistId,
                            t1.artistName,
                            t1.imageUrl,
                            t1.popularity
                        FROM
                            artists t1
                        JOIN
                            artist_genres t2 ON t2.artistId = t1.artistId AND t2.genre IN %s
                    ) t1
                    JOIN event_artists t2 ON t2.artistId = t1.artistId
                    JOIN events t3 ON t3.eventId = t2.eventId AND t3.eventStartLocalDate >= NOW() AND t3.eventStatus IN ('onsale', 'offsale')
                    JOIN event_classifications t4 ON (t4.eventId = t3.eventId AND t4.classificationSegment = 'Music')
                    JOIN user_locations t5 ON (t5.userId = %s)
                    LEFT JOIN event_venues t6 ON (t6.eventId = t3.eventId AND lat_lng_distance(t6.venueLatitude, t6.venueLongitude, t5.latitude, t5.longitude) <= 50)
                    GROUP BY 1,2,3,4
                    HAVING COUNT(t3.eventId) >= 1 AND COUNT(t6.eventId) >= 1
                    ORDER BY 4 DESC
                    LIMIT 100
                ) t1
                JOIN
                    artist_genres t2 ON t2.artistId = t1.artistId
                GROUP BY 1,2,3,4,5,6
                ORDER BY 4 DESC
                """, [terms, user])

                data = self.dictfetchall(cursor)

                if data:

                    for i in data:
                        i['genres'] = i['genres'].split(',')

            else:

                data = []
                for i in terms:
                    i = '%'+i+'%'
                    cursor.execute("""
                        SELECT
                            t1.artistId AS 'artist_id',
                            t1.artistName AS 'artist_name',
                            t1.popularity,
                            t1.imageUrl AS 'image_url',
                            GROUP_CONCAT(DISTINCT t2.genre) AS 'genres',
                            COUNT(DISTINCT t4.eventId) AS 'total_count'
                        FROM artists t1
                        JOIN artist_genres t2 ON t1.artistId=t2.artistId
                        JOIN event_artists t3 ON t1.artistId=t3.artistId
                        JOIN events t4 ON t3.eventId=t4.eventId AND eventStatus IN ('onsale','offsale') AND eventStartLocalDate >= Now()
                        JOIN event_classifications t5 ON t5.eventId=t4.eventId AND t5.classificationSegment='Music'
                        WHERE t1.artistName LIKE %s
                        GROUP BY 1 ORDER BY 3 DESC LIMIT 100
                    """, [i])

                    for artist in self.dictfetchall(cursor):
                        artist['genres'] = artist['genres'].split(',')
                        data.append(artist)

            return Response(data=data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
