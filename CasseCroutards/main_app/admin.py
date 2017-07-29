from django.contrib import admin
from .models import Trip, User, Order

# Register your models here.

admin.site.register(Trip)
admin.site.register(User)
admin.site.register(Order)