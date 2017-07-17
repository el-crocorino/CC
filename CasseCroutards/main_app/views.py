from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .models import Trip
from .forms import TripForm


# Create your views here.

def index( request):
	trips = Trip.objects.all
	addTripForm = TripForm
	return render(request, 'index.html', {'trips': trips, 'addTripForm' : addTripForm})

def trip_detail( request, tripId):
	trip = Trip.objects.get(id = tripId)
	return render(request, 'trip_detail.html', {'trip': trip})
		
def trip_add( request):

	form = TripForm( request.POST)

	if form.is_valid():
		trip = form.save( commit = False)
		trip.user = request.user
		trip.save()

	return HttpResponseRedirect('/')
		
def trip_delete( request, tripId):

	trip = Trip.objects.get( id = tripId)
	trip.delete()

	return HttpResponseRedirect('/')
		
def trip_update( request, tripId):
	pass

def profile( request, username):
	pass
	