# Generated by Django 2.0.4 on 2018-05-11 07:56

from django.db import migrations
import lisztfeverapp.artists.models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0020_auto_20180508_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artists',
            name='updatedat',
        ),
        migrations.AddField(
            model_name='artists',
            name='updated_at',
            field=lisztfeverapp.artists.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True),
        ),
        migrations.AlterModelTable(
            name='artists',
            table=None,
        ),
    ]
