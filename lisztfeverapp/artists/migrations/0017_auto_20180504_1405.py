# Generated by Django 2.0.4 on 2018-05-04 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_venue'),
        ('artists', '0016_auto_20180504_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(db_column='artistId', on_delete=django.db.models.deletion.CASCADE, to='artists.Artists')),
                ('event', models.ForeignKey(db_column='eventId', on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='artists',
            name='events',
            field=models.ManyToManyField(through='artists.ArtistEvent', to='events.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='artistevent',
            unique_together={('artist', 'event')},
        ),
    ]
