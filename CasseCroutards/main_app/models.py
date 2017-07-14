from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trip( models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    city_start = models.CharField( max_length = 100)
    city_end = models.CharField( max_length = 100)
    max_amount = models.DecimalField( max_digits = 6, decimal_places = 2)
    created = models.DateTimeField( auto_now_add = True)
    updated = models.DateTimeField( auto_now_add = True)
    
class Order( models.Model):
    user = models.ForeignKey(User)
    

class Item( models.Model):
    order = models.ForeignKey(Order)
    

class Appointment( models.Model):
    order = models.ForeignKey(Order)
    
    