from django.shortcuts import render
from main_app.models import Trip, Order
from main_app.forms import TripForm, TripItemForm

def index( pRequest):
    '''
    Homepage
    '''
    trips = Trip.objects.all()

    for trip in trips:
        trip.getOrders(pRequest.user.id)
        trip.getItems()

    addTripForm = TripForm( prefix = 'TripForm')
    addTripItemForm = TripItemForm( prefix = 'TripItemForm')
    
    return render(pRequest, 'index.html', {
        'trips': trips, 
        'addTripForm' : addTripForm, 
        'addTripItemForm' : addTripItemForm, 
        'showTripUser': True, 
        'showTripOrder': True, 
        'showOrderUser': True,
        'showOrderTrip': False,
        'showExtendedTripItems': False,
        })