from rest_framework import serializers
from . import models
# from lisztfeverapp.events import serializers as event_serializers
# If above line activated, events serializer cannot get artist serializer

class ArtistGenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ArtistGenres
        fields = (
            "id",
            "genre",
        )

class ArtistSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Artists
        fields = (
            "artistid",
            "artistname",
            "imageurl",
        )


class ArtistAllSerializer(serializers.ModelSerializer):

    # genres = ArtistGenresSerializer(many=True)

    class Meta:
        model = models.Artists
        fields = (
            "artistid",
            "artistname",
            "attractionid",
            "popularity",
            "followers",
            "externalurl",
            "imageurl",
            "updatedat",
            # "genres",
        )
