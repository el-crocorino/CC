from django.contrib import admin
from django.core import urlresolvers
from main_app.models import Trip, TripItem, User, Order

# Register your models here.



class TripAdmin( admin.ModelAdmin):
    '''
    Admin Trip class
    '''
    list_display = ['id', 'user', 'date', 'city_start', 'city_end', 'amount_limit', 'created', 'updated']

class TripItemAdmin( admin.ModelAdmin):
    '''
    Admin TripItem class
    '''
    list_display = ['id', 'trip', 'title', 'average_value', 'average_qty', 'created', 'updated']
    
    '''
    See : 
    https://stackoverflow.com/questions/163823/can-list-display-in-a-django-modeladmin-display-attributes-of-foreignkey-field
    https://stackoverflow.com/questions/28832897/link-in-django-admin-to-foreign-key-object
    
    list_display = ['id', 'link_to_Trip', 'title', 'average_value', 'average_qty', 'created', 'updated']

    def link_to_Trip(self, obj):
        link = urlresolvers.reverse("admin:trip", args = [obj.trip.id]) #model name has to be lowercase
        return u'<a href="%s">%s</a>' % (link, obj.trip.name)
    link_to_Trip.allow_tags = True
    '''


class UserAdmin( admin.ModelAdmin):
    '''
    Admin User class
    '''
    list_display = ['id', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_active', 'location', 'ratio', 'created', 'updated']


class OrderAdmin( admin.ModelAdmin):
    '''
    Admin Order class
    '''
    list_display = ['id', 'user', 'trip', 'amount', 'status', 'created', 'updated']



admin.site.register(Trip, TripAdmin)
admin.site.register(TripItem, TripItemAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)