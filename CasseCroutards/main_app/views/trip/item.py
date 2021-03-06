from django.shortcuts import render

from main_app.models import Trip, Order


def trip_item( pRequest, pTripId):
    '''
    Detailed trip view

    @param int pTripId Trip id
    '''
    trip = Trip.objects.get( id = pTripId)
    #trip.orders = Order.objects.filter( trip = pTripId)
    trip.getOrders(pRequest.user.id)
    trip.getItems() 
    
    return render(pRequest, 'trip/item.html', {
        'trip': trip, 
        'showTripUser': True, 
        'showTripOrder': True, 
        'showOrderUser': True,
        'showOrderTrip': False,
        'showExtendedTripItems': True,
        })