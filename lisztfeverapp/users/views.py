from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.contrib.humanize.templatetags.humanize import naturalday
from django.conf import settings
from django.core.paginator import Paginator
from django.db import connection
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

cursor = connection.cursor()

# class UserMain(APIView):
#
#     def get(self, request, format=None):
#
#         page = request.query_params.get('page', None)
#
#         if page:
#
#             try:
#                 found_artist = artist_models.Artists.objects.all()
#             except artist_models.Artists.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#
#             paginator = Paginator(found_artist, 10)
#
#             total_pages = paginator.num_pages
#
#             artists = paginator.get_page(page)
#
#             serializer = artist_serializers.ArtistAllSerializer(artists, many=True)
#
#             results = {}
#
#             results.update({"total_pages": total_pages})
#
#             results.update({"data": serializer.data})
#
#             return Response(data=results, status=status.HTTP_200_OK)
#
#         else:
#
#             return Response(status=status.HTTP_400_BAD_REQUEST)

class UserMain(APIView):

    def get(self, request, format=None):

        user = request.user

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
            """, [user])

        data = self.dictfetchall(cursor)

        if data:

            for i in data:
                i['genres'] = i['genres'].split(',')

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
        user_plan = user.user_events.all().filter(eventstartlocaldate__gte=date.today()).order_by('eventstartlocaldate')
        event_serializer = event_serializers.EventSerializer(user_plan, many=True, context={'request': request})

        result = []
        for i in event_serializer.data:
            venue_added_event = {}
            try:
                found_venue = event_models.EventVenues.objects.filter(eventid=i['eventid'])
            except event_models.EventVenues.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            venue_serializer = event_serializers.EventVenuesSerializer(found_venue, many=True)

            venue = []
            for j in venue_serializer.data:
                venue.append(dict(OrderedDict(j)))

            http_to_https = i.get('primaryeventurl')
            if http_to_https and http_to_https[:5] == 'http:':
                http_to_https = 'https:' + http_to_https[5:]
                i['primaryeventurl'] = http_to_https

            venue_added_event.update({'event':i, 'venue': venue})
            result.append(venue_added_event)

        return Response(data=result, status=status.HTTP_200_OK)

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
