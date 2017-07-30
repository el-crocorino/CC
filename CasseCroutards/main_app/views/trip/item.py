from django.shortcuts import render
from main_app.models import Trip, Order


def trip_item( pRequest, pTripId):
    '''
    Detailed trip view

    @param int pTripId Trip id
    '''
    trip = Trip.objects.get( id = pTripId)
    trip.orders = Order.objects.filter( trip = pTripId)
    print(trip.orders)
    print(trip.__dict__)
    return render(pRequest, 'trip/item.html', {'trip': trip})