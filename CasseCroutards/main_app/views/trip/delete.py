from django.http import HttpResponseRedirect
from main_app.models import Trip


        
def trip_delete( pRequest, pTripId):

    trip = Trip.objects.get( id = pTripId)
    trip.delete()

    return HttpResponseRedirect('/')