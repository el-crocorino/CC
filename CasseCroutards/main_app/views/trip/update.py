from django.shortcuts import render

from main_app.models import Trip
from main_app.forms import TripForm

def trip_update( pRequest, pTripId):

    if pRequest.method == 'POST': 

        form = TripForm( pRequest.POST)

        if form.is_valid():

            trip = Trip.objects.get( id = pTripId)

            trip.date = form.cleaned_data['date']
            trip.city_start = form.cleaned_data['city_start']
            trip.city_end = form.cleaned_data['city_end']
            trip.amount_limit = form.cleaned_data['amount_limit']
            trip.participants_limit = form.cleaned_data['participants_limit']
            trip.comment = form.cleaned_data['comment']

            trip.save()
            return render(pRequest, 'trip/item.html', {'trip': trip})

    else:
        trip = Trip.objects.get( id = pTripId)
        updateTripForm = TripForm( initial = {
            'date' : trip.date, 
            'city_start' : trip.city_start, 
            'city_end' : trip.city_end, 
            'amount_limit' : trip.amount_limit, 
            'participants_limit' : trip.participants_limit, 
            'comment' : trip.comment
            })
        
        return render(pRequest, 'trip/update.html', {'trip': trip,'updateTripForm' : updateTripForm}) 