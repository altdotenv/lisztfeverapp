# Generated by Django 2.0.4 on 2018-04-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20180412_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='event_ids',
        ),
        migrations.AddField(
            model_name='plan',
            name='event_id',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
