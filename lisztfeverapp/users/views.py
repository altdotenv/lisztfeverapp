from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.conf import settings
from django.core.paginator import Paginator
from .models import User #cookiecutter default
from . import models, serializers
from lisztfeverapp.artists import models as artist_models
from lisztfeverapp.events import serializers as event_serializers
from lisztfeverapp.artists import serializers as artist_serializers
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from facepy import SignedRequest
import json

class UserMain(APIView):

    def get(self, request, format=None):

        page = request.query_params.get('page', None)

        if page:

            try:
                found_artist = artist_models.Artists.objects.all()
            except artist_models.Artists.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            paginator = Paginator(found_artist, 10)

            total_pages = paginator.num_pages

            artists = paginator.get_page(page)

            serializer = artist_serializers.ArtistAllSerializer(artists, many=True)

            results = {}

            results.update({"total_pages": total_pages})

            results.update({"data": serializer.data})

            return Response(data=results, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserPlan(APIView):

    def get(self, request, format=None):

        user = request.user
        user_plan = user.user_events.all()
        serializer = event_serializers.EventSerializer(user_plan, many=True, context={'request': request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserSetting(APIView):

    def get(self, request, format=None): #format=None is json format

        user_id = request.user.id
        user = models.User.objects.filter(id=user_id)
        serializer = serializers.UserSerializer(user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

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
