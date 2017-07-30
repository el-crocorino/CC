from django.shortcuts import render
from main_app.models import Trip, Order
from main_app.forms import TripForm

def index( pRequest):
    '''
    Homepage
    '''
    trips = Trip.objects.all()
    for trip in trips:
        trip.orders = Order.objects.filter( trip = trip.id)

    addTripForm = TripForm
    return render(pRequest, 'index.html', {'trips': trips, 'addTripForm' : addTripForm})