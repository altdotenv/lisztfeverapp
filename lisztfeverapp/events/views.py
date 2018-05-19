from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from lisztfeverapp.users import models as user_models
from lisztfeverapp.artists import models as artist_models
from collections import OrderedDict
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

        if artist_id is not None:

            try:
                found_event = models.Events.objects.raw("""
                    SELECT *
                    FROM events t1
                    INNER JOIN event_artists t2
                    ON t1.eventId=t2.eventId
                    WHERE t2.artistId=%s
                """, [artist_id])
            except models.Events.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            event_serializer = serializers.EventSerializer(found_event, many=True, context={'request': request})

            result = []
            for i in event_serializer.data:
                venue_added_event = {}
                try:
                    found_venue = models.EventVenues.objects.filter(eventid=i['eventid'])
                except models.EventVenues.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                venue_serializer = serializers.EventVenuesSerializer(found_venue, many=True)

                venue = []
                for j in venue_serializer.data:
                    venue.append(dict(OrderedDict(j)))

                venue_added_event.update({'event':i, 'venue': venue})
                result.append(venue_added_event)

            return Response(data=result, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

class PlanEvent(APIView):

    def post(self, request, event_id, format=None):

        user = request.user

        try:
            found_event = models.Events.objects.get(eventid=event_id)
        except models.Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_plan = user_models.Plan.objects.get(
                user=user,
                event=found_event
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except user_models.Plan.DoesNotExist:

            new_plan = user_models.Plan.objects.create(
                user=user,
                event=found_event
            )
            new_plan.save()

            return Response(status=status.HTTP_201_CREATED)

class UnPlanEvent(APIView):

    def delete(self, request, event_id, format=None):

        user = request.user

        try:
            found_event = models.Events.objects.get(eventid=event_id)
        except models.Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_plan = user_models.Plan.objects.get(
                user=user,
                event=found_event
            )
            preexisting_plan.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except user_models.Plan.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)
