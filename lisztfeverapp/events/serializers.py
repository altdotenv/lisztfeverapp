from rest_framework import serializers
from . import models
from lisztfeverapp.users import models as user_models
from lisztfeverapp.artists import serializers as artist_serializers

class EventVenuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EventVenues
        fields = (
            "venueid",
            "venuename",
            "venuecity",
            "venuestatecode",
            "venuecountrycode",
            "venuestreet",
            "venuezipcode",
            "venuelatitude",
            "venuelongitude",
            "venueurl",
            "venuetimezone",
        )


class EventSerializer(serializers.ModelSerializer):

    # artists = artist_serializers.ArtistSerializer(source="artists_set", many=True)
    is_planned = serializers.SerializerMethodField()

    class Meta:
        model = models.Events
        fields = (
            "eventid",
            "eventname",
            "eventstartlocaldate",
            "eventimageurl",
            "primaryeventurl",
            "eventstatus",
            "maxprice",
            "minprice",
            # "artists",
            "is_planned",
        )

    def get_is_planned(self, obj):
        if 'request' in self.context:
            request = self.context['request']
            try:
                user_models.Plan.objects.get(
                    user__id=request.user.id, event__eventid=obj.eventid)
                return True
            except user_models.Plan.DoesNotExist:
                return False
        return False
        
