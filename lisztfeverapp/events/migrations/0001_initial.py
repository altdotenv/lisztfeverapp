# Generated by Django 2.0.4 on 2018-05-30 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventArtists',
            fields=[
                ('eventid', models.CharField(db_column='eventId', max_length=255, primary_key=True, serialize=False)),
                ('artistid', models.CharField(db_column='artistId', max_length=255)),
                ('artistname', models.CharField(blank=True, db_column='artistName', max_length=255, null=True)),
                ('attractionid', models.CharField(blank=True, db_column='attractionId', max_length=255, null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'event_artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventAttractions',
            fields=[
                ('eventid', models.CharField(db_column='eventId', max_length=255, primary_key=True, serialize=False)),
                ('attractionid', models.CharField(db_column='attractionId', max_length=255)),
                ('attractionimageurl', models.CharField(blank=True, db_column='attractionImageUrl', max_length=255, null=True)),
                ('attractionname', models.CharField(db_column='attractionName', max_length=255)),
                ('attractionurl', models.CharField(blank=True, db_column='attractionUrl', max_length=255, null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'event_attractions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventClassifications',
            fields=[
                ('eventid', models.CharField(db_column='eventId', max_length=255, primary_key=True, serialize=False)),
                ('classificationsegment', models.CharField(blank=True, db_column='classificationSegment', max_length=255, null=True)),
                ('classificationgenre', models.CharField(blank=True, db_column='classificationGenre', max_length=255, null=True)),
                ('classificationsubgenre', models.CharField(blank=True, db_column='classificationSubGenre', max_length=255, null=True)),
                ('classificationsubtype', models.CharField(blank=True, db_column='classificationSubType', max_length=255, null=True)),
                ('classificationtype', models.CharField(blank=True, db_column='classificationType', max_length=255, null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'event_classifications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventid', models.CharField(db_column='eventId', max_length=255, primary_key=True, serialize=False)),
                ('eventimageurl', models.CharField(blank=True, db_column='eventImageUrl', max_length=255, null=True)),
                ('eventname', models.CharField(blank=True, db_column='eventName', max_length=255, null=True)),
                ('eventstartlocaldate', models.DateField(blank=True, db_column='eventStartLocalDate', null=True)),
                ('eventstatus', models.CharField(blank=True, db_column='eventStatus', max_length=50, null=True)),
                ('onsaleenddatetime', models.DateTimeField(blank=True, db_column='onsaleEndDateTime', null=True)),
                ('onsalestartdatetime', models.DateTimeField(blank=True, db_column='onsaleStartDateTime', null=True)),
                ('primaryeventurl', models.CharField(blank=True, db_column='primaryEventUrl', max_length=1024, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('currency', models.CharField(blank=True, max_length=50, null=True)),
                ('maxprice', models.FloatField(blank=True, db_column='maxPrice', null=True)),
                ('minprice', models.FloatField(blank=True, db_column='minPrice', null=True)),
                ('eventstartlocaltime', models.TimeField(blank=True, db_column='eventStartLocalTime', null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventVenues',
            fields=[
                ('eventid', models.CharField(db_column='eventId', max_length=255, primary_key=True, serialize=False)),
                ('venueid', models.CharField(db_column='venueId', max_length=255)),
                ('venuename', models.CharField(blank=True, db_column='venueName', max_length=1024, null=True)),
                ('venuecity', models.CharField(blank=True, db_column='venueCity', max_length=255, null=True)),
                ('venuestatecode', models.CharField(blank=True, db_column='venueStateCode', max_length=50, null=True)),
                ('venuecountrycode', models.CharField(blank=True, db_column='venueCountryCode', max_length=50, null=True)),
                ('venuestreet', models.CharField(blank=True, db_column='venueStreet', max_length=1024, null=True)),
                ('venuezipcode', models.CharField(blank=True, db_column='venueZipCode', max_length=255, null=True)),
                ('venuelatitude', models.FloatField(blank=True, db_column='venueLatitude', null=True)),
                ('venuelongitude', models.FloatField(blank=True, db_column='venueLongitude', null=True)),
                ('venueurl', models.CharField(blank=True, db_column='venueUrl', max_length=1024, null=True)),
                ('venuetimezone', models.CharField(blank=True, db_column='venueTimezone', max_length=255, null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'event_venues',
                'managed': False,
            },
        ),
    ]
