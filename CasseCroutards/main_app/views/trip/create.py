from django.http import HttpResponseRedirect

#from main_app.models import Trip
from main_app.forms import TripForm



def trip_create( pRequest):

    form = TripForm( pRequest.POST)

    if form.is_valid():
        trip = form.save( commit = False)
        trip.user = pRequest.user
        trip.save()

    return HttpResponseRedirect('/')