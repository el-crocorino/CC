from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from main_app.models import Trip

@login_required
def trip_delete( pRequest, pTripId):
    '''
    Trip deletion view
    @param int pTripId Trip id
    '''
    # TODO : add check request user == trip user
    trip = Trip.objects.get( id = pTripId)
    trip.delete()

    return HttpResponseRedirect('/')