from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from lisztfeverapp.artists import models as artist_models
from lisztfeverapp.events import models as event_models
from datetime import datetime
from time import strftime

class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """
    def __init__(self, null=False, blank=False, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to
        # cheat a little:
        self.blank, self.isnull = blank, null
        self.null = True # To prevent the framework from shoving in "not null".

    def db_type(self, connection):
        typ=['TIMESTAMP']
        # See above!
        if self.isnull:
            typ += ['NULL']
        if self.auto_created:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        else:
            return models.DateTimeField.to_python(self, value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value==None:
            return None
        # Use '%Y%m%d%H%M%S' for MySQL < 4.1
        return strftime('%Y-%m-%d %H:%M:%S',value.timetuple())


class User(AbstractBaseUser):

    """ User Model """

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )
    username = models.CharField(_('username'), max_length=255, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    first_name = models.CharField(max_length=255, db_column='firstName', null=True)
    last_name = models.CharField(max_length=255, db_column='lastName', null=True)
    page_id = models.CharField(max_length=255, db_column='pageId', null=True)
    profile_pic = models.URLField(db_column='profilePic', max_length=1025, null=True)
    timezone = models.IntegerField(null=True)
    locale = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True)
    updated_at = UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)
    created_at = UnixTimestampField(db_column='createdAt', null=True)
    last_session_at = UnixTimestampField(db_column='lastSessionAt', null=True)
    sessions = models.IntegerField(null=True, default=0)
    user_events = models.ManyToManyField(event_models.Events, through='Plan', related_name="user_events")

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username


class Plan(models.Model):

    user = models.ForeignKey(User, db_column='userId', to_field='username', on_delete=models.CASCADE, related_name='user_plans') #Without related_name default is plan_set
    event = models.ForeignKey(event_models.Events, db_column='eventId', on_delete=models.CASCADE)
    updated_at = UnixTimestampField(auto_created=True, db_column='updatedAt', null=True)

    class Meta:
        unique_together = (('user', 'event'),)
