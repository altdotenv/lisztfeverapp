from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from lisztfeverapp.users import models as user_models
from lisztfeverapp.artists import models as artist_models
# Create your views here.

class Event(APIView):

    def get(self, request, event_id, format=None):

        try:
            found_event = models.Event.objects.get(eventid=event_id)
        except models.Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.EventSerializer(found_event)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EventByArtistId(APIView):

    def get(self, request, artist_id, format=None):

        if artist_id is not None:

            found_event = models.Event.objects.filter(artists__artistid=artist_id)
            serializer = serializers.EventSerializer(found_event, many=True, context={'request': request})

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class PlanEvent(APIView):

    def post(self, request, event_id, format=None):

        user = request.user

        try:
            found_event = models.Event.objects.get(eventid=event_id)
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
            found_event = models.Event.objects.get(eventid=event_id)
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
