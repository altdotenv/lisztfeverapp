# Generated by Django 2.0.4 on 2018-05-11 07:56

from django.db import migrations
import lisztfeverapp.events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180511_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='updatedat',
        ),
        migrations.AddField(
            model_name='event',
            name='updated_at',
            field=lisztfeverapp.events.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True),
        ),
    ]