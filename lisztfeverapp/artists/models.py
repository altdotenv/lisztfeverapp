from django.db import models
from lisztfeverapp.events import models as event_models
# Create your models here.

class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """
    def __init__(self, null=False, blank=False, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to
        # cheat a little:
        self.blank, self.isnull = blank, null
        self.null = True # To prevent the framework from shoving in "not null".

    def db_type(self, connection):
        typ=['TIMESTAMP']
        # See above!
        if self.isnull:
            typ += ['NULL']
        if self.auto_created:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        else:
            return models.DateTimeField.to_python(self, value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value==None:
            return None
        # Use '%Y%m%d%H%M%S' for MySQL < 4.1
        return strftime('%Y-%m-%d %H:%M:%S',value.timetuple())

class Genre(models.Model):

    genre = models.CharField(max_length=50)
    updated_at = UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)

class Artists(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
    artistname = models.CharField(db_column='artistName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attractionid = models.CharField(db_column='attractionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    popularity = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    updated_at = UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)
    imageurl = models.CharField(db_column='imageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    events = models.ManyToManyField(event_models.Event, through='ArtistEvent')
    genres = models.ManyToManyField(Genre, through='ArtistGenre')

    class Meta:
        ordering = ['-popularity']

class ArtistGenre(models.Model):

    artist = models.ForeignKey(Artists, db_column='artistId', on_delete=models.CASCADE, max_length=50)
    genre = models.ForeignKey(Genre, db_column='genre', on_delete=models.CASCADE, max_length=50)
    updated_at = UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)

    class Meta:
        unique_together = (('artist', 'genre'),)

class ArtistEvent(models.Model):

    artist = models.ForeignKey(Artists, db_column='artistId', on_delete=models.CASCADE)
    event = models.ForeignKey(event_models.Event, db_column='eventId', on_delete=models.CASCADE)
    artistname = models.CharField(db_column='artistName', max_length=255, blank=True, null=True)
    attractionid = models.CharField(db_column='attractionId', max_length=255, blank=True, null=True)
    updated_at = UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)

    class Meta:
        unique_together = (('artist', 'event'),)

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

class ArtistGenres(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=50)  # Field name made lowercase.
    genre = models.CharField(max_length=50)
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'artist_genres'
        unique_together = (('artistid', 'genre'),)

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


class RelatedArtists(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=50)  # Field name made lowercase.
    relatedartistid = models.CharField(db_column='relatedArtistId', max_length=50)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'related_artists'
        unique_together = (('artistid', 'relatedartistid'),)
