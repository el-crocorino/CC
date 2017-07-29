from django.shortcuts import render
from main_app.models import Trip


def trip_item( pRequest, pTripId):
    '''
    Detailed trip view

    @param int pTripId Trip id
    '''
    trip = Trip.objects.get( id = pTripId)
    return render(pRequest, 'trip/item.html', {'trip': trip})