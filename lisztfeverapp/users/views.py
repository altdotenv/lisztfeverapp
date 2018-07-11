from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.contrib.humanize.templatetags.humanize import naturalday
from django.conf import settings
from django.core.paginator import Paginator
from .models import User #cookiecutter default
from . import models, serializers
from lisztfeverapp.artists import models as artist_models
from lisztfeverapp.events import serializers as event_serializers, models as event_models
from lisztfeverapp.artists import serializers as artist_serializers
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from facepy import SignedRequest
import json
from datetime import date, timedelta, datetime
from collections import OrderedDict
import boto3
from django.db import connection
from .. import tracker

class UserMain(APIView):

    def get(self, request, format=None):

        user = request.user

        query = """
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
                FROM artists t1
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
            """

        with connection.cursor() as cursor:
            cursor.execute(query, [user])
            data = self.dictfetchall(cursor)
            if not data or not len(data):
                return Response(status=status.HTTP_409_CONFLICT)

        if data:

            for i in data:
                i['genres'] = i['genres'].split(',')

        tracker.WebLogs.user_click(self, user.username, request.path, request.META['HTTP_REFERER'])

        return Response(data=data, status=status.HTTP_200_OK)

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class UserPlan(APIView):

    def get(self, request, format=None):

        user = request.user

        query = """
            SELECT
              t2.eventId AS 'eventid',
              t2.eventName AS 'eventname',
              t2.eventStartLocalDate AS 'eventstartlocaldate',
              t2.eventImageUrl AS 'eventimageurl',
              t2.primaryEventUrl AS 'primaryeventurl',
              t2.eventStatus AS 'eventstatus',
              GROUP_CONCAT(t3.venueId SEPARATOR '||') AS 'venueid',
              GROUP_CONCAT(t3.venueName SEPARATOR '||') AS 'venuename',
              GROUP_CONCAT(t3.venueCity SEPARATOR '||') AS 'venuecity',
              GROUP_CONCAT(t3.venueStreet SEPARATOR '||') AS 'venuestreet'
            FROM users_plan t1
            JOIN events t2 ON t1.eventId=t2.eventId AND t2.eventStartLocalDate >= NOW()
            JOIN event_venues t3 ON t2.eventId=t3.eventId
            WHERE t1.userId=%s
            GROUP BY 1
            ORDER BY 3 ASC
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [user])
            data = self.dictfetchall(cursor)

        result = []

        if data:

            for i in data:

                if i.get('venueid'):
                    split_venueid = i['venueid'].split('||')
                    split_venuename = i['venuename'].split('||') if i.get('venuename') else ['Not Specified']
                    split_venuecity = i['venuecity'].split('||') if i.get('venuecity') else ['Not Specified']
                    split_venuestreet = i['venuestreet'].split('||') if i.get('venuestreet') else ['Not Specified']
                    i.pop('venueid')
                    i.pop('venuename')
                    i.pop('venuecity')
                    i.pop('venuestreet')


                venue = []
                for venueid, venuename, venuecity, venuestreet in zip(split_venueid, split_venuename, split_venuecity, split_venuestreet):
                    single_venue = {}
                    single_venue.update({
                        'venueid':venueid,
                        'venuename':venuename,
                        'venuecity':venuecity,
                        'venuestreet':venuestreet
                    })
                    venue.append(single_venue)

                is_planned = self.get_is_planned(user, i['eventid'])
                i.update({'is_planned':is_planned})

                http_to_https = i.get('primaryeventurl')
                if http_to_https and http_to_https[:5] == 'http:':
                    http_to_https = 'https:' + http_to_https[5:]
                    i['primaryeventurl'] = http_to_https

                venue_added_event = {}
                venue_added_event.update({'event':i, 'venue': venue})
                result.append(venue_added_event)

        tracker.WebLogs.user_click(self, user.username, request.path, None)

        return Response(data=result, status=status.HTTP_200_OK)

    def get_is_planned(self, user, event_id):

        try:
            models.Plan.objects.get(
                user=user, event=event_id)
            return True
        except models.Plan.DoesNotExist:
            return False

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


# class UserPlan(APIView):
#
#     def get(self, request, format=None):
#
#         user = request.user
#         user_plan = user.user_events.all().filter(eventstartlocaldate__gte=date.today()).order_by('eventstartlocaldate')
#         event_serializer = event_serializers.EventSerializer(user_plan, many=True, context={'request': request})
#
#         result = []
#         for i in event_serializer.data:
#             venue_added_event = {}
#             try:
#                 found_venue = event_models.EventVenues.objects.filter(eventid=i['eventid'])
#             except event_models.EventVenues.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#
#             venue_serializer = event_serializers.EventVenuesSerializer(found_venue, many=True)
#
#             venue = []
#             for j in venue_serializer.data:
#                 venue.append(dict(OrderedDict(j)))
#
#             http_to_https = i.get('primaryeventurl')
#             if http_to_https and http_to_https[:5] == 'http:':
#                 http_to_https = 'https:' + http_to_https[5:]
#                 i['primaryeventurl'] = http_to_https
#
#             venue_added_event.update({'event':i, 'venue': venue})
#             result.append(venue_added_event)
#
#         return Response(data=result, status=status.HTTP_200_OK)

class UserSetting(APIView):

    def get(self, request, format=None): #format=None is json format

        user_id = request.user.id
        user = models.User.objects.filter(id=user_id)
        serializer = serializers.UserSerializer(user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class FacebookListenMusic(APIView):

    def get(self, request, artist_id, format=None): #format=None is json format

        user_id = request.user.username

        if not user_id:

            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if artist_id:

            try:
                self.invoke_lambda(user_id, artist_id)
            except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            tracker.WebLogs.listen_music(self, user_id, artist_id)

            return Response(status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    def invoke_lambda(self, user_id, artist_id):

        lambda_client = boto3.client('lambda', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, region_name='us-east-1')
        event = {
                'entry':[
                            {'messaging':
                                [
                                    {
                                        'timestamp': int(datetime.utcnow().strftime("%s")),
                                        'postback': {'payload': artist_id, 'title': 'Listen Music'},
                                        'recipient': {'id': '421790108259470'},
                                        'sender': {'id': user_id}
                                    }
                                ]
                            }
                        ]
                }

        invoke_response = lambda_client.invoke(
            FunctionName = 'lisztfever',
            InvocationType = 'Event',
            Payload = json.dumps(event)
        )

        if invoke_response['StatusCode'] not in [200, 202, 204]:

            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class FacebookSignedRequest(APIView):

    permission_classes = []

    def post(self, request, format=None):

        try:
            signed_request = json.loads(request.body)['signed_request']
            signed_request_data = SignedRequest.parse(signed_request, settings.FB_APP_SECRET)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = models.User.objects.get(username=signed_request_data['psid'])
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        token = {'token':token}

        return Response(data=token, status=status.HTTP_200_OK)
