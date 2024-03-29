# Generated by Django 2.0.4 on 2018-05-30 06:30

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import lisztfeverapp.users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', lisztfeverapp.users.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(db_column='firstName', max_length=255, null=True)),
                ('last_name', models.CharField(db_column='lastName', max_length=255, null=True)),
                ('page_id', models.CharField(db_column='pageId', max_length=255, null=True)),
                ('profile_pic', models.URLField(db_column='profilePic', max_length=1025, null=True)),
                ('timezone', models.IntegerField(null=True)),
                ('locale', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('not-specified', 'Not specified')], max_length=50, null=True)),
                ('created_at', lisztfeverapp.users.models.UnixTimestampField(db_column='createdAt', null=True)),
                ('last_session_at', lisztfeverapp.users.models.UnixTimestampField(db_column='lastSessionAt', null=True)),
                ('sessions', models.IntegerField(default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', lisztfeverapp.users.models.UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)),
                ('event', models.ForeignKey(db_column='eventId', on_delete=django.db.models.deletion.CASCADE, to='events.Events')),
                ('user', models.ForeignKey(db_column='userId', on_delete=django.db.models.deletion.CASCADE, related_name='user_plans', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_events',
            field=models.ManyToManyField(related_name='user_events', through='users.Plan', to='events.Events'),
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together={('user', 'event')},
        ),
    ]
