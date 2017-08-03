from django.contrib import admin
from main_app.models import Trip, User, Order

# Register your models here.



class TripAdmin( admin.ModelAdmin):
    '''
    Admin Order class
    '''
    list_display = ['id', 'user', 'date', 'city_start', 'city_end', 'amount_limit', 'created', 'updated']


class UserAdmin( admin.ModelAdmin):
    '''
    Admin Order class
    '''
    list_display = ['id', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_active', 'location', 'ratio', 'created', 'updated']


class OrderAdmin( admin.ModelAdmin):
    '''
    Admin Order class
    '''
    list_display = ['id', 'user', 'trip', 'amount', 'status', 'created', 'updated']



admin.site.register(Trip, TripAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)