# Generated by Django 2.0.4 on 2018-04-14 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_auto_20180414_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistevents',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='artistevents',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RemoveField(
            model_name='artistevents',
            name='artistname',
        ),
        migrations.RemoveField(
            model_name='artistevents',
            name='attractionid',
        ),
    ]
