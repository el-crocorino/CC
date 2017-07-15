from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Trip


# Create your views here.

def index(request):
	trips = Trip.objects.all
	return render(request, 'index.html', {'trips': trips})

def trip_detail(request, tripId):
	trip = Trip.objects.get(id = tripId)
	return render(request, 'trip_detail.html', {'trip': trip})
		
def trip_add(request):
	pass