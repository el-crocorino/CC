from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from main_app.forms import TripForm

@login_required
def trip_create( pRequest):
    '''
    Trip creation view
    '''

    form = TripForm( pRequest.POST)

    if form.is_valid():
        trip = form.save( commit = False)
        trip.user = pRequest.user
        trip.save()

    return HttpResponseRedirect('/')