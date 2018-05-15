# Generated by Django 2.0.4 on 2018-05-15 01:10

from django.db import migrations, models
import django.db.models.deletion
import lisztfeverapp.artists.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumTracks',
            fields=[
                ('albumid', models.CharField(db_column='albumId', max_length=255, primary_key=True, serialize=False)),
                ('trackid', models.CharField(db_column='trackId', max_length=255)),
                ('trackname', models.CharField(blank=True, db_column='trackName', max_length=255, null=True)),
                ('externalurl', models.CharField(blank=True, db_column='externalUrl', max_length=1024, null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'album_tracks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArtistAlbums',
            fields=[
                ('artistid', models.CharField(db_column='artistId', max_length=255, primary_key=True, serialize=False)),
                ('albumid', models.CharField(db_column='albumId', max_length=255)),
                ('albumname', models.CharField(blank=True, db_column='albumName', max_length=255, null=True)),
                ('albumtype', models.CharField(blank=True, db_column='albumType', max_length=50, null=True)),
                ('externalurl', models.CharField(blank=True, db_column='externalUrl', max_length=1024, null=True)),
                ('imageurl', models.CharField(blank=True, db_column='imageUrl', max_length=1024, null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
                ('releasedate', models.DateTimeField(blank=True, db_column='releaseDate', null=True)),
                ('releasedateprecision', models.CharField(blank=True, db_column='releaseDatePrecision', max_length=50, null=True)),
            ],
            options={
                'db_table': 'artist_albums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArtistFeatures',
            fields=[
                ('artistid', models.CharField(db_column='artistId', max_length=255, primary_key=True, serialize=False)),
                ('tempo', models.FloatField(blank=True, null=True)),
                ('energy', models.FloatField(blank=True, null=True)),
                ('speechiness', models.FloatField(blank=True, null=True)),
                ('instrumentalness', models.FloatField(blank=True, null=True)),
                ('duration_ms', models.FloatField(blank=True, null=True)),
                ('liveness', models.FloatField(blank=True, null=True)),
                ('acousticness', models.FloatField(blank=True, null=True)),
                ('loudness', models.FloatField(blank=True, null=True)),
                ('valence', models.FloatField(blank=True, null=True)),
                ('danceability', models.FloatField(blank=True, null=True)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'artist_features',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArtistGenres',
            fields=[
                ('artistid', models.CharField(db_column='artistId', max_length=50, primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=50)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'artist_genres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelatedArtists',
            fields=[
                ('artistid', models.CharField(db_column='artistId', max_length=50, primary_key=True, serialize=False)),
                ('relatedartistid', models.CharField(db_column='relatedArtistId', max_length=50)),
                ('updatedat', models.DateTimeField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'related_artists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArtistEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', lisztfeverapp.artists.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)),
                ('artistname', models.CharField(blank=True, db_column='artistName', max_length=255, null=True)),
                ('attractionid', models.CharField(blank=True, db_column='attractionId', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', lisztfeverapp.artists.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('updated_at', lisztfeverapp.artists.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)),
                ('artistid', models.CharField(db_column='artistId', max_length=255, primary_key=True, serialize=False)),
                ('artistname', models.CharField(blank=True, db_column='artistName', max_length=255, null=True)),
                ('attractionid', models.CharField(blank=True, db_column='attractionId', max_length=255, null=True)),
                ('popularity', models.IntegerField(blank=True, null=True)),
                ('followers', models.IntegerField(blank=True, null=True)),
                ('externalurl', models.CharField(blank=True, db_column='externalUrl', max_length=1024, null=True)),
                ('imageurl', models.CharField(blank=True, db_column='imageUrl', max_length=255, null=True)),
                ('events', models.ManyToManyField(through='artists.ArtistEvent', to='events.Event')),
            ],
            options={
                'ordering': ['-popularity'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', lisztfeverapp.artists.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='artists',
            name='genres',
            field=models.ManyToManyField(through='artists.ArtistGenre', to='artists.Genre'),
        ),
        migrations.AddField(
            model_name='artistgenre',
            name='artist',
            field=models.ForeignKey(db_column='artistId', max_length=50, on_delete=django.db.models.deletion.CASCADE, to='artists.Artists'),
        ),
        migrations.AddField(
            model_name='artistgenre',
            name='genre',
            field=models.ForeignKey(db_column='genre', max_length=50, on_delete=django.db.models.deletion.CASCADE, to='artists.Genre'),
        ),
        migrations.AddField(
            model_name='artistevent',
            name='artist',
            field=models.ForeignKey(db_column='artistId', on_delete=django.db.models.deletion.CASCADE, to='artists.Artists'),
        ),
        migrations.AddField(
            model_name='artistevent',
            name='event',
            field=models.ForeignKey(db_column='eventId', on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='artistgenre',
            unique_together={('artist', 'genre')},
        ),
        migrations.AlterUniqueTogether(
            name='artistevent',
            unique_together={('artist', 'event')},
        ),
    ]
