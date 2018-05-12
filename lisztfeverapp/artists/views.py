from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from lisztfeverapp.users import models as user_models
# from django.db import connection
# cursor = connection.cursor()
# Create your views here.

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

            genres = genres.split(",")
            found_artist = models.Artists.objects.filter(genres__genre__in=genres).distinct()

            serializer = serializers.ArtistAllSerializer(found_artist, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class FollowArtist(APIView):

    def post(self, request, artist_id, format=None):

        user = request.user

        try:
            found_artist = models.Artists.objects.get(artistid=artist_id)
        except models.Artists.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_follow = user_models.FollowArtist.objects.get(
                user=user,
                artist=found_artist,
                source="webapp",
                classification="explore",
                follow=1
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except user_models.FollowArtist.DoesNotExist:

            new_follow = user_models.FollowArtist.objects.create(
                user=user,
                artist=found_artist,
                source="webapp",
                classification="explore",
                follow=1
            )
            new_follow.save()

            return Response(status=status.HTTP_201_CREATED)

class UnFollowArtist(APIView):

    def delete(self, request, artist_id, format=None):

        user=request.user

        try:
            found_artist = models.Artists.objects.get(artistid=artist_id)
        except models.Artists.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_follow = user_models.FollowArtist.objects.get(
                user=user,
                artist=found_artist,
                source="webapp",
                classification="explore",
                follow=1
            )
            preexisting_follow.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except user_models.FollowArtist.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)
