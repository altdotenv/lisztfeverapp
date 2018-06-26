from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from lisztfeverapp.users import models as user_models
from lisztfeverapp.artists import models as artist_models
from collections import OrderedDict
from django.db import connection

# Create your views here.

class Event(APIView):

    def get(self, request, event_id, format=None):

        try:
            found_event = models.Events.objects.get(eventid=event_id)
        except models.Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            found_venue = models.EventVenues.objects.filter(eventid=event_id)
        except models.EventVenues.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        event_serializer = serializers.EventSerializer(found_event, context={'request': request})
        venue_serializer = serializers.EventVenuesSerializer(found_venue, many=True)

        venue = []
        for i in venue_serializer.data:
            venue.append(dict(OrderedDict(i)))

        result = {'event':event_serializer.data, 'venue':venue}

        return Response(data=result, status=status.HTTP_200_OK)


class EventByArtistId(APIView):

    def get(self, request, artist_id, format=None):

        user = request.user

        if artist_id and user:

            query = """
                SELECT
                    t2.eventId AS 'event_id',
                    t2.eventName AS 'event_name',
                    t2.eventImageUrl AS 'event_image_url',
                    t2.eventStartLocalDate AS 'event_start_local_date',
                    t2.eventStartLocalTime AS 'event_start_local_time',
                    t2.eventStatus AS 'event_status',
                    t2.primaryEventUrl AS 'primary_event_url',
                    GROUP_CONCAT(t3.venueName SEPARATOR '||') AS 'venue_name',
                    GROUP_CONCAT(t3.venueCity SEPARATOR '||') AS 'venue_city',
                    CASE WHEN (lat_lng_distance(t3.venueLatitude, t3.venueLongitude, t5.latitude, t5.longitude) <= 50) THEN 1
                        ELSE 2 END AS 'near'
                FROM event_artists t1
                JOIN events t2 ON (t2.eventId=t1.eventId AND t1.artistId= %s AND eventStartLocalDate >= NOW() AND t2.eventStatus IN ('onsale', 'offsale'))
                JOIN event_venues t3 ON (t3.eventId=t2.eventId)
                JOIN event_classifications t4 ON t4.eventId=t2.eventId AND t4.classificationSegment='Music'
                JOIN user_locations t5 ON (t5.userId= %s)
                GROUP BY 1
                ORDER BY 10 ASC, 4 ASC
            """

            with connection.cursor() as cursor:
                cursor.execute(query, [artist_id, user])
                data = self.dictfetchall(cursor)
                if not data or not len(data):
                    return Response(status=status.HTTP_409_CONFLICT)

            for i in data:

                venue_list = []
                venue_name_list = i['venue_name'].split('||')
                venue_city_list = i['venue_city'].split('||')
                i.pop('venue_name')
                i.pop('venue_city')
                for name, city in zip(venue_name_list, venue_city_list):
                    venue = {}
                    venue.update({'venue_name':name, 'venue_city':city})
                    venue_list.append(venue)

                i.update({'venues':venue_list})

                is_planned = self.get_is_planned(user, i['event_id'])
                i.update({'is_planned':is_planned})

                http_to_https = i.get('primary_event_url')
                if http_to_https and http_to_https[:5] == 'http:':
                    http_to_https = 'https:' + http_to_https[5:]
                    i['primary_event_url'] = http_to_https

                i['event_start_local_time'] = str(i['event_start_local_time'])[:5]

            return Response(data=data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_is_planned(self, user, event_id):

        try:
            user_models.Plan.objects.get(
                user=user, event=event_id)
            return True
        except user_models.Plan.DoesNotExist:
            return False

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class PlanEvent(APIView):

    def post(self, request, event_id, format=None):

        user = request.user.username

        try:
            found_event = models.Events.objects.get(eventid=event_id)
        except models.Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_plan = user_models.Plan.objects.get(
                user=user,
                event=found_event.eventid
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except user_models.Plan.DoesNotExist:

            new_plan = user_models.Plan.objects.create(
                user=user,
                event=found_event.eventid
            )
            new_plan.save()

            return Response(status=status.HTTP_201_CREATED)

class UnPlanEvent(APIView):

    def delete(self, request, event_id, format=None):

        user = request.user.username

        try:
            found_event = models.Events.objects.get(eventid=event_id)
        except models.Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_plan = user_models.Plan.objects.get(
                user=user,
                event=found_event.eventid
            )
            preexisting_plan.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except user_models.Plan.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)
