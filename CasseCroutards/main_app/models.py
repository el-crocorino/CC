from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User( AbstractBaseUser, PermissionsMixin):

    email = models.EmailField( _( 'email address'), unique = True)
    first_name = models.CharField( _( 'first name'), max_length=30, blank = True)
    last_name = models.CharField( _( 'last name'), max_length=30, blank = True)
    date_joined = models.DateTimeField( _( 'date joined'), auto_now_add = True)
    is_staff = models.BooleanField(
        _('staff status'),
        default = False,
        help_text = _('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default = True,
        help_text = _(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    
    location = models.CharField( max_length = 100, blank = True)
    bio = models.TextField( max_length = 1500, blank = True)
    avatar = models.ImageField( upload_to = 'avatars/', default = 'media/default-avatar.svg')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _( 'user')
        verbose_name_plural = _( 'users')

    def get_full_name( self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % ( self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name( self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user( self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail( subject, message, from_email, [self.email], **kwargs)

class Trip( models.Model):

    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    date = models.DateField()
    city_start = models.CharField( max_length = 100)
    city_end = models.CharField( max_length = 100)
    amount_limit = models.DecimalField( max_digits = 6, decimal_places = 2)
    participants_limit = models.IntegerField( default = 0)
    comment = models.TextField( max_length = 1500, default = '')
    created = models.DateTimeField( auto_now_add = True)
    updated = models.DateTimeField( auto_now_add = True)
    
    def __str__( self):
        description = self.date.strftime("%B %d, %Y") + ' ' + self.city_start[:10]
        if len(self.city_start) > 10:
            description += '...'
        description += '-' + self.city_end[:10]
        if len(self.city_end) > 10:
            description += '...'
        return description
    
class Order( models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    

class Item( models.Model):
    order = models.ForeignKey( Order)
    

class Appointment( models.Model):
    order = models.ForeignKey( Order)