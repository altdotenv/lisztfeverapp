from django.db import models
from lisztfeverapp.events import models as event_models

# Create your models here.
class Artists(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
    artistname = models.CharField(db_column='artistName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attractionid = models.CharField(db_column='attractionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    popularity = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    events = models.ManyToManyField(event_models.Event, through='ArtistEvent')

    class Meta:
        db_table = 'artists'
        ordering = ['-popularity']

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ArtistEvent(TimeStampedModel):

    artist = models.ForeignKey(Artists, db_column='artistId', on_delete=models.CASCADE)
    event = models.ForeignKey(event_models.Event, db_column='eventId', on_delete=models.CASCADE)

class AlbumTracks(models.Model):
    albumid = models.CharField(db_column='albumId', primary_key=True, max_length=255)  # Field name made lowercase.
    trackid = models.CharField(db_column='trackId', max_length=255)  # Field name made lowercase.
    trackname = models.CharField(db_column='trackName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'album_tracks'
        unique_together = (('albumid', 'trackid'),)


class ArtistAlbums(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
    albumid = models.CharField(db_column='albumId', max_length=255)  # Field name made lowercase.
    albumname = models.CharField(db_column='albumName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    albumtype = models.CharField(db_column='albumType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    releasedate = models.DateTimeField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
    releasedateprecision = models.CharField(db_column='releaseDatePrecision', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'artist_albums'
        unique_together = (('artistid', 'albumid'),)


class ArtistFeatures(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
    tempo = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    speechiness = models.FloatField(blank=True, null=True)
    instrumentalness = models.FloatField(blank=True, null=True)
    duration_ms = models.FloatField(blank=True, null=True)
    liveness = models.FloatField(blank=True, null=True)
    acousticness = models.FloatField(blank=True, null=True)
    loudness = models.FloatField(blank=True, null=True)
    valence = models.FloatField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'artist_features'


class ArtistGenres(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=50)  # Field name made lowercase.
    genre = models.CharField(max_length=50)
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'artist_genres'
        unique_together = (('artistid', 'genre'),)


class RelatedArtists(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=50)  # Field name made lowercase.
    relatedartistid = models.CharField(db_column='relatedArtistId', max_length=50)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'related_artists'
        unique_together = (('artistid', 'relatedartistid'),)
