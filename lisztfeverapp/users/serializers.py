from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from . import models
from lisztfeverapp.events import serializers as event_serializers
# from lisztfeverapp.artists import serializers as artist_serializers

class PlanSerializer(serializers.ModelSerializer):

    event = event_serializers.EventSerializer()

    class Meta:
        model = models.Plan
        fields = (
            "id",
            "event",
        )

class UserSerializer(serializers.ModelSerializer):

    user_plans = PlanSerializer(many=True)
    # user_follow_artists = FollowArtistSerializer(many=True)

    class Meta:
        model = models.User
        fields = (
            'id',
            'name',
            'username',
            'profile_image',
            "event_count",
            'user_plans',
        )

class SignUpSerializer(RegisterSerializer):

    name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user
