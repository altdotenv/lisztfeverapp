from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime

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

class Venue(models.Model):
    venueid = models.CharField(db_column='venueId', primary_key=True, max_length=255)  # Field name made lowercase.
    venuecity = models.CharField(db_column='venueCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    venuecountrycode = models.CharField(db_column='venueCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    venuename = models.CharField(db_column='venueName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    venuetimezone = models.CharField(db_column='venueTimezone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    venuestreet = models.CharField(db_column='venueStreet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    venuezipcode = models.CharField(db_column='venueZipCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    venuelatitude = models.FloatField(db_column='venueLatitude', blank=True, null=True)  # Field name made lowercase.
    venuelongitude = models.FloatField(db_column='venueLongitude', blank=True, null=True)  # Field name made lowercase.
    venueurl = models.CharField(db_column='venueUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    venuestatecode = models.CharField(db_column='venueStateCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venues'


class Event(models.Model):
    eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
    eventimageurl = models.CharField(db_column='eventImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eventname = models.CharField(db_column='eventName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eventstartlocaldate = models.DateField(db_column='eventStartLocalDate', blank=True, null=True)  # Field name made lowercase.
    eventstatus = models.CharField(db_column='eventStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    onsaleenddatetime = models.DateTimeField(db_column='onsaleEndDateTime', blank=True, null=True)  # Field name made lowercase.
    onsalestartdatetime = models.DateTimeField(db_column='onsaleStartDateTime', blank=True, null=True)  # Field name made lowercase.
    primaryeventurl = models.CharField(db_column='primaryEventUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=50, blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    maxprice = models.FloatField(db_column='maxPrice', blank=True, null=True)  # Field name made lowercase.
    minprice = models.FloatField(db_column='minPrice', blank=True, null=True)  # Field name made lowercase.
    eventstartlocaltime = models.TimeField(db_column='eventStartLocalTime', blank=True, null=True)  # Field name made lowercase.
    updated_at = UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)
    venue = models.ForeignKey(Venue, db_column='venueId', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['eventstartlocaldate']

class EventArtists(models.Model):
    eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
    artistid = models.CharField(db_column='artistId', max_length=255)  # Field name made lowercase.
    artistname = models.CharField(db_column='artistName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attractionid = models.CharField(db_column='attractionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_artists'
        unique_together = (('eventid', 'artistid'),)


class EventAttractions(models.Model):
    eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
    attractionid = models.CharField(db_column='attractionId', max_length=255)  # Field name made lowercase.
    attractionimageurl = models.CharField(db_column='attractionImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attractionname = models.CharField(db_column='attractionName', max_length=255)  # Field name made lowercase.
    attractionurl = models.CharField(db_column='attractionUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_attractions'
        unique_together = (('eventid', 'attractionid'),)


class EventClassifications(models.Model):
    eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
    classificationsegment = models.CharField(db_column='classificationSegment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classificationgenre = models.CharField(db_column='classificationGenre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classificationsubgenre = models.CharField(db_column='classificationSubGenre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classificationsubtype = models.CharField(db_column='classificationSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classificationtype = models.CharField(db_column='classificationType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_classifications'


class EventVenues(models.Model):
    eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
    venueid = models.CharField(db_column='venueId', max_length=255)  # Field name made lowercase.
    venuename = models.CharField(db_column='venueName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    venuecity = models.CharField(db_column='venueCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    venuestatecode = models.CharField(db_column='venueStateCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    venuecountrycode = models.CharField(db_column='venueCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    venuestreet = models.CharField(db_column='venueStreet', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    venuezipcode = models.CharField(db_column='venueZipCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    venuelatitude = models.FloatField(db_column='venueLatitude', blank=True, null=True)  # Field name made lowercase.
    venuelongitude = models.FloatField(db_column='venueLongitude', blank=True, null=True)  # Field name made lowercase.
    venueurl = models.CharField(db_column='venueUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    venuetimezone = models.CharField(db_column='venueTimezone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_venues'
        unique_together = (('eventid', 'venueid'),)
