from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from lisztfeverapp.artists import models as artist_models
from lisztfeverapp.events import models as event_models


class User(AbstractUser):

    """ User Model """

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    profile_image = models.ImageField(null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    user_events = models.ManyToManyField(event_models.Event, through='Plan', related_name="user_events")
    # following_artists = models.ManyToManyField(artist_models.Artists, through='followArtist', related_name="follow_artists")

    def __str__(self):
        return self.username

    @property
    def event_count(self):
        return self.user_events.all().count()

    # @property
    # def following_count(self):
    #     return self.following_artists.all().count()


class TimeStampedModel(models.Model):

    updated_at = models.DateTimeField(db_column='updatedAt', auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class Plan(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_plans') #Without related_name default is plan_set
    event = models.ForeignKey(event_models.Event, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-updated_at']

# class FollowArtist(TimeStampedModel):
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_follow_artists') #Without related_name default is followartist_set
#     artist = models.ForeignKey(artist_models.Artists, on_delete=models.CASCADE)
#     source = models.CharField(max_length=64, null=True)
#     classification = models.CharField(max_length=64, null=True)
#     follow = models.IntegerField(null=True)
#
#     class Meta:
#         ordering = ['-created_at']
