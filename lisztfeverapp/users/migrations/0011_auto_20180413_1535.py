# Generated by Django 2.0.4 on 2018-04-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180413_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='track_artists',
            field=models.ManyToManyField(through='users.TrackArtist', to='artists.Artists'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_events',
            field=models.ManyToManyField(through='users.Plan', to='events.Events'),
        ),
    ]
