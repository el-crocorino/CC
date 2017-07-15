from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trip( models.Model):
    user = models.ForeignKey(User)
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
    user = models.ForeignKey(User)
    

class Item( models.Model):
    order = models.ForeignKey(Order)
    

class Appointment( models.Model):
    order = models.ForeignKey(Order)

class UserProfile( models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField( max_length = 254)
    avatar = models.ImageField( upload_to = 'profile_images', default = 'media/default.png')
    
    def __str__(self):
        return self.user.username