# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class AlbumTracks(models.Model):
#     albumid = models.CharField(db_column='albumId', primary_key=True, max_length=255)  # Field name made lowercase.
#     trackid = models.CharField(db_column='trackId', max_length=255)  # Field name made lowercase.
#     trackname = models.CharField(db_column='trackName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'album_tracks'
#         unique_together = (('albumid', 'trackid'),)
#
#
# class ArtistAlbums(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
#     albumid = models.CharField(db_column='albumId', max_length=255)  # Field name made lowercase.
#     albumname = models.CharField(db_column='albumName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     albumtype = models.CharField(db_column='albumType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     imageurl = models.CharField(db_column='imageUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     releasedate = models.DateTimeField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
#     releasedateprecision = models.CharField(db_column='releaseDatePrecision', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'artist_albums'
#         unique_together = (('artistid', 'albumid'),)
#
#
# class ArtistFeatures(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
#     tempo = models.FloatField(blank=True, null=True)
#     energy = models.FloatField(blank=True, null=True)
#     speechiness = models.FloatField(blank=True, null=True)
#     instrumentalness = models.FloatField(blank=True, null=True)
#     duration_ms = models.FloatField(blank=True, null=True)
#     liveness = models.FloatField(blank=True, null=True)
#     acousticness = models.FloatField(blank=True, null=True)
#     loudness = models.FloatField(blank=True, null=True)
#     valence = models.FloatField(blank=True, null=True)
#     danceability = models.FloatField(blank=True, null=True)
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'artist_features'
#
#
# class ArtistGenres(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=50)  # Field name made lowercase.
#     genre = models.CharField(max_length=50)
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'artist_genres'
#         unique_together = (('artistid', 'genre'),)
#
#
# class Artists(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
#     artistname = models.CharField(db_column='artistName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     attractionid = models.CharField(db_column='attractionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     popularity = models.IntegerField(blank=True, null=True)
#     followers = models.IntegerField(blank=True, null=True)
#     externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     imageurl = models.CharField(db_column='imageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'artists'
#
#
# class DeleteAlbums(models.Model):
#     albumid = models.CharField(db_column='albumId', primary_key=True, max_length=255)  # Field name made lowercase.
#     reason = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'delete_albums'
#
#
# class EventArtists(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     artistid = models.CharField(db_column='artistId', max_length=255)  # Field name made lowercase.
#     artistname = models.CharField(db_column='artistName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     attractionid = models.CharField(db_column='attractionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'event_artists'
#         unique_together = (('eventid', 'artistid'),)
#
#
# class EventAttractions(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     attractionid = models.CharField(db_column='attractionId', max_length=255)  # Field name made lowercase.
#     attractionimageurl = models.CharField(db_column='attractionImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     attractionname = models.CharField(db_column='attractionName', max_length=255)  # Field name made lowercase.
#     attractionurl = models.CharField(db_column='attractionUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'event_attractions'
#         unique_together = (('eventid', 'attractionid'),)
#
#
# class EventClassifications(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     classificationsegment = models.CharField(db_column='classificationSegment', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classificationgenre = models.CharField(db_column='classificationGenre', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classificationsubgenre = models.CharField(db_column='classificationSubGenre', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classificationsubtype = models.CharField(db_column='classificationSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classificationtype = models.CharField(db_column='classificationType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'event_classifications'
#
#
# class EventVenues(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     venueid = models.CharField(db_column='venueId', max_length=255)  # Field name made lowercase.
#     venuename = models.CharField(db_column='venueName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     venuecity = models.CharField(db_column='venueCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuestatecode = models.CharField(db_column='venueStateCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     venuecountrycode = models.CharField(db_column='venueCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     venuestreet = models.CharField(db_column='venueStreet', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     venuezipcode = models.CharField(db_column='venueZipCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuelatitude = models.FloatField(db_column='venueLatitude', blank=True, null=True)  # Field name made lowercase.
#     venuelongitude = models.FloatField(db_column='venueLongitude', blank=True, null=True)  # Field name made lowercase.
#     venueurl = models.CharField(db_column='venueUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     venuetimezone = models.CharField(db_column='venueTimezone', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'event_venues'
#         unique_together = (('eventid', 'venueid'),)
#
#
# class Events(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     eventimageurl = models.CharField(db_column='eventImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     eventname = models.CharField(db_column='eventName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     eventstartlocaldate = models.DateField(db_column='eventStartLocalDate', blank=True, null=True)  # Field name made lowercase.
#     eventstatus = models.CharField(db_column='eventStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     onsaleenddatetime = models.DateTimeField(db_column='onsaleEndDateTime', blank=True, null=True)  # Field name made lowercase.
#     onsalestartdatetime = models.DateTimeField(db_column='onsaleStartDateTime', blank=True, null=True)  # Field name made lowercase.
#     primaryeventurl = models.CharField(db_column='primaryEventUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     source = models.CharField(max_length=50, blank=True, null=True)
#     currency = models.CharField(max_length=50, blank=True, null=True)
#     maxprice = models.FloatField(db_column='maxPrice', blank=True, null=True)  # Field name made lowercase.
#     minprice = models.FloatField(db_column='minPrice', blank=True, null=True)  # Field name made lowercase.
#     eventstartlocaltime = models.TimeField(db_column='eventStartLocalTime', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'events'
#
#
# class FeatureMetrics(models.Model):
#     feature = models.CharField(primary_key=True, max_length=50)
#     mean = models.FloatField(blank=True, null=True)
#     std = models.FloatField(blank=True, null=True)
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'feature_metrics'
#
#
# class RelatedArtists(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=50)  # Field name made lowercase.
#     relatedartistid = models.CharField(db_column='relatedArtistId', max_length=50)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'related_artists'
#         unique_together = (('artistid', 'relatedartistid'),)
#
#
# class SlotTypes(models.Model):
#     type = models.CharField(primary_key=True, max_length=255)
#     value = models.CharField(max_length=255)
#     colname = models.CharField(db_column='colName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tablename = models.CharField(db_column='tableName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'slot_types'
#         unique_together = (('type', 'value'),)
#
#
# class TopTrackFeatures(models.Model):
#     trackid = models.CharField(db_column='trackId', primary_key=True, max_length=255)  # Field name made lowercase.
#     tempo = models.FloatField(blank=True, null=True)
#     energy = models.FloatField(blank=True, null=True)
#     speechiness = models.FloatField(blank=True, null=True)
#     instrumentalness = models.FloatField(blank=True, null=True)
#     duration_ms = models.IntegerField(blank=True, null=True)
#     liveness = models.FloatField(blank=True, null=True)
#     acousticness = models.FloatField(blank=True, null=True)
#     loudness = models.FloatField(blank=True, null=True)
#     valence = models.FloatField(blank=True, null=True)
#     danceability = models.FloatField(blank=True, null=True)
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'top_track_features'
#
#
# class TopTracks(models.Model):
#     trackid = models.CharField(db_column='trackId', primary_key=True, max_length=255)  # Field name made lowercase.
#     artistid = models.CharField(db_column='artistId', max_length=255)  # Field name made lowercase.
#     popularity = models.IntegerField(blank=True, null=True)
#     externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     trackname = models.CharField(db_column='trackName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     imageurl = models.CharField(db_column='imageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'top_tracks'
#         unique_together = (('trackid', 'artistid'),)
#
#
# class UserActions(models.Model):
#     userid = models.CharField(db_column='userId', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     action = models.CharField(max_length=255)
#     source = models.CharField(max_length=50, blank=True, null=True)
#     contenttype = models.CharField(db_column='contentType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     contentid = models.CharField(db_column='contentId', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     value = models.CharField(max_length=255, blank=True, null=True)
#     positionx = models.IntegerField(db_column='positionX', blank=True, null=True)  # Field name made lowercase.
#     positiony = models.IntegerField(db_column='positionY', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'user_actions'
#
#
# class UserArtistFollows(models.Model):
#     userid = models.CharField(db_column='userId', primary_key=True, max_length=255)  # Field name made lowercase.
#     artistid = models.CharField(db_column='artistId', max_length=255)  # Field name made lowercase.
#     source = models.CharField(max_length=50, blank=True, null=True)
#     classification = models.CharField(max_length=255)
#     follow = models.IntegerField()
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'user_artist_follows'
#         unique_together = (('userid', 'artistid', 'classification'),)
#
#
# class UserLocations(models.Model):
#     userid = models.CharField(db_column='userId', primary_key=True, max_length=255)  # Field name made lowercase.
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'user_locations'
#
#
# class UserSubscriptions(models.Model):
#     userid = models.CharField(db_column='userId', primary_key=True, max_length=255)  # Field name made lowercase.
#     subscriptiontype = models.CharField(db_column='subscriptionType', max_length=255)  # Field name made lowercase.
#     subscription = models.IntegerField()
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
# 
#     class Meta:
#         managed = False
#         db_table = 'user_subscriptions'
#         unique_together = (('userid', 'subscriptiontype'),)
#
#
# class Users(models.Model):
#     userid = models.CharField(db_column='userId', primary_key=True, max_length=255)  # Field name made lowercase.
#     pageid = models.CharField(db_column='pageId', max_length=255)  # Field name made lowercase.
#     firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     lastname = models.CharField(db_column='lastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(max_length=50, blank=True, null=True)
#     locale = models.CharField(max_length=50, blank=True, null=True)
#     profilepic = models.CharField(db_column='profilePic', max_length=1025, blank=True, null=True)  # Field name made lowercase.
#     timezone = models.IntegerField(blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     lastsessionat = models.DateTimeField(db_column='lastSessionAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'users'
#         unique_together = (('userid', 'pageid'),)
#
#
# class Venues(models.Model):
#     venueid = models.CharField(db_column='venueId', primary_key=True, max_length=255)  # Field name made lowercase.
#     venuecity = models.CharField(db_column='venueCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     venuecountrycode = models.CharField(db_column='venueCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     venuename = models.CharField(db_column='venueName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuetimezone = models.CharField(db_column='venueTimezone', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuestreet = models.CharField(db_column='venueStreet', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuezipcode = models.CharField(db_column='venueZipCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuelatitude = models.FloatField(db_column='venueLatitude', blank=True, null=True)  # Field name made lowercase.
#     venuelongitude = models.FloatField(db_column='venueLongitude', blank=True, null=True)  # Field name made lowercase.
#     venueurl = models.CharField(db_column='venueUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuestatecode = models.CharField(db_column='venueStateCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'venues'
