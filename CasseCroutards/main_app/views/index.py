from django.shortcuts import render
from main_app.models import Trip
from main_app.forms import TripForm

def index( pRequest):
    '''
    Homepage
    '''
    trips = Trip.objects.all
    addTripForm = TripForm
    return render(pRequest, 'index.html', {'trips': trips, 'addTripForm' : addTripForm})