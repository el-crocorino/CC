from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .models import Trip, UserProfile
from .forms import TripForm


# Create your views here.

def index( request):
	trips = Trip.objects.all
	addTripForm = TripForm
	return render(request, 'index.html', {'trips': trips, 'addTripForm' : addTripForm})

def user_create( request):
	pass

def user_profile( request):
	pass

def user_update( request):
	pass

def user_delete( request):
	pass

def trip_detail( request, tripId):
	trip = Trip.objects.get(id = tripId)
	return render(request, 'trip_detail.html', {'trip': trip})
		
def trip_create( request):

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

	trip = Trip.objects.get( id = tripId)
	addTripForm = TripForm( initial = {
		'date' : trip.date, 
		'city_start' : trip.city_start, 
		'city_end' : trip.city_end, 
		'amount_limit' : trip.amount_limit, 
		'participants_limit' : trip.participants_limit, 
		'comment' : trip.comment
		})
	
	return render(request, 'trip_update.html', {'trip': trip,'addTripForm' : addTripForm})

def profile( request, username):
	pass
	