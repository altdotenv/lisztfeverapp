from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from lisztfeverapp.users import models as user_models

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

        genres = request.query_params.get('genres', None)

        if genres is not None:

            genres = tuple(genres.split(","))
            found_artist = models.Artists.objects.raw("""
                SELECT *
                FROM artists t1
                INNER JOIN artist_genres t2
                ON t1.artistId = t2.artistId
                WHERE t2.genre IN %s
            """, [genres]).distinct()

            serializer = serializers.ArtistAllSerializer(found_artist, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
