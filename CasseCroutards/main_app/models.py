import datetime

from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User( AbstractBaseUser, PermissionsMixin):
    '''
    User Model
    '''

    email = models.EmailField( _( 'email address'), unique = True)
    first_name = models.CharField( _( 'first name'), max_length = 30, blank = True)
    last_name = models.CharField( _( 'last name'), max_length = 30, blank = True)
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
    
    location = models.CharField( _( 'location'), max_length = 100, blank = True)
    birth_date = models.DateField( _( 'birth date'), default = datetime.date.today)
    bio = models.TextField( _( 'presentation'), max_length = 1500, blank = True)
    avatar = models.ImageField( _( 'avatar'), upload_to = 'media/avatars/', default = 'media/default-avatar.png', blank = True)
    ratio = models.DecimalField( _( 'ratio'), default = 0, max_digits = 6, decimal_places = 2)
    created = models.DateTimeField( auto_now_add = True)
    updated = models.DateTimeField( auto_now_add = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'main_app'
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

    def email_user( self, subject, message, from_email = None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail( subject, message, from_email, [self.email], **kwargs)

class Trip( models.Model):
    '''
    Trip Model
    '''
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    date = models.DateField( _( 'tripDate'))
    city_start = models.CharField( _( 'tripCityStart'), max_length = 100)
    city_end = models.CharField( _( 'tripCityEnd'), max_length = 100)
    amount_limit = models.DecimalField( _( 'tripMaxAmount'), max_digits = 6, decimal_places = 2)
    participants_limit = models.IntegerField( _( 'tripMaxParticipants'), default = 0)
    comment = models.TextField( _( 'tripDescription'), max_length = 1500, default = '')
    created = models.DateTimeField( _( 'created'), auto_now_add = True)
    updated = models.DateTimeField( _( 'updated'), auto_now_add = True)

    class Meta:
        app_label = 'main_app'
    
    def __str__( self):
        description = self.date.strftime("%B %d, %Y") + ' ' + self.city_start[:10]
        if len(self.city_start) > 10:
            description += '...'
        description += '-' + self.city_end[:10]
        if len(self.city_end) > 10:
            description += '...'
        return description

    def getOrders(self, pUserId):
        '''
        Gets trip orders list and checks if user has already placed one
    
        @param int pUserId User id    
        '''

        self.orders = Order.objects.filter( trip = self.id)

        for order in self.orders:
            
            if order.user.id == pUserId:
                self.currentUserHasOrder = True
                self.currentUserOrder = order
            else:
                self.currentUserHasOrder = False

            order.statusAsText = order.get_status_display()

    def getItems(self):
        '''
        Gets trip items
        '''
        self.items = TripItem.objects.filter( trip = self.id)
    
class Order( models.Model):
    '''
    Order Model
    '''    
    REFUSED = 0
    PENDING = 1
    ACCEPTED = 2
    RUNNING = 3
    HONORED = 4

    Status = (
        (REFUSED, 'refused'),
        (PENDING, 'pending'),
        (ACCEPTED, 'accepted'),
        (RUNNING, 'running'),
        (HONORED, 'honored'),
        )

    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    trip = models.ForeignKey( Trip, on_delete = models.CASCADE)
    comment = models.TextField( _( 'orderDescription'), max_length = 1500, default = '')
    amount = models.DecimalField( _( 'orderAmount'), max_digits = 5, decimal_places = 2, default = 0.00)
    status = models.IntegerField( _( 'orderStatus'), choices = Status, default = PENDING)
    created = models.DateTimeField( _( 'created'), auto_now_add = True)
    updated = models.DateTimeField( _( 'updated'), auto_now_add = True)

    class Meta:
        app_label = 'main_app'
    
    def __str__( self):
        return str(self.id) + ' | ' + self.user.first_name + ' - ' + str(self.amount) + ': ' + str(self.get_status_display())

    def get_status_display( self):   
        return self.Status[self.status][1]

class TripItem( models.Model):
    '''
    Trip Item Model
    Gets displayed in trip to offer user a selected list of goods
    '''
    trip = models.ForeignKey( Trip)
    title = models.TextField( _( 'tripItemTitle'), max_length = 150)
    description = models.TextField( _( 'tripItemDescription'), max_length = 500)
    average_value = models.DecimalField( _( 'tripItemAVGValue'), max_digits = 5, decimal_places = 2, default = 0.00, blank = True)
    average_qty = models.IntegerField( _( 'tripItemAVGQty'), default = 0, blank = True)
    created = models.DateTimeField( _( 'created'), auto_now_add = True)
    updated = models.DateTimeField( _( 'updated'), auto_now_add = True)

    class Meta:
        app_label = 'main_app'
    
    def __str__( self):
        return str(self.id) + ' | ' + self.title

class OrderItem( models.Model):
    '''
    Order Item Model
    Refers to a TripItem object : a user can order a specific item as listed in Trip object
    '''
    tripItem = models.ForeignKey( TripItem)
    order = models.ForeignKey( Order)
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    amount = models.DecimalField( _( 'orderItemAmount'), max_digits = 5, decimal_places = 2, default = 0.00)
    quantity = models.IntegerField( _( 'orderItemQty'), default = 1)
    created = models.DateTimeField( _( 'created'), auto_now_add = True)
    updated = models.DateTimeField( _( 'updated'), auto_now_add = True)

    class Meta:
        app_label = 'main_app'
    
    def __str__( self):
        return str(self.id) + ' | ' + self.user.first_name + ' : ' + self.tripItem.title + ' - ' + str(self.amount) + '/ ' + str(self.quantity)
    

class Appointment( models.Model):
    '''
    Appointment Model
    '''
    order = models.ForeignKey( Order)

    class Meta:
        app_label = 'main_app'


class Comment( models.Model):
    '''
    Comment Model 

    TODO Later in CC-43
    See : https://medium.com/@bhrigu/django-how-to-add-foreignkey-to-multiple-models-394596f06e84
    '''
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #parentId = models.ForeignKey( Order)
    text = models.TextField( max_length = 1500, default = '')
    created = models.DateTimeField( auto_now_add = True)
    updated = models.DateTimeField( auto_now_add = True)


    class Meta:
        app_label = 'main_app'

