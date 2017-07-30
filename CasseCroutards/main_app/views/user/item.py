from django.shortcuts import render
from django.contrib.auth import get_user_model

from main_app.models import Trip, Order

def user_item( pRequest, pUserId):
    '''
    Detailed user view

    @param int pUserId User id
    '''
    user = get_user_model().objects.get( id = pUserId)
    trips = Trip.objects.filter( user = user)
    orders = Order.objects.filter( user = user)
    return render(pRequest, 'user/item.html', {
        'user': user, 
        'trips': trips, 
        'orders': orders, 
        'showTripUser': False, 
        'showOrderUser': False,
        'showOrderTrip': True
        })