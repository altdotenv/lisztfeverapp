# Generated by Django 2.0.4 on 2018-05-16 03:38

from django.db import migrations
import lisztfeverapp.events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='updatedat',
            field=lisztfeverapp.events.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True),
        ),
    ]
