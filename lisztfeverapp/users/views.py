from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from .models import User #cookiecutter default
from . import models, serializers
from lisztfeverapp.artists import models as artist_models
from lisztfeverapp.events import serializers as event_serializers
from lisztfeverapp.artists import serializers as artist_serializers
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
import base64
import hashlib
import hmac
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

class SignedRequest(APIView):

    def post(self, request, format=None):

        signed_request = dict(request.POST)['signed_request'][0]
        data = parse_signed_request(signed_request, "d1b796668ef444802a7f4dcb910b0ca1")
        print (data)
