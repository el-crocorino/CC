from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from main_app.forms import TripForm, TripItemForm

@login_required
def trip_create( pRequest):
    '''
    Trip creation view
    '''

    tripForm = TripForm( pRequest.POST, prefix = "TripForm")

    if tripForm.is_valid():

        tripItemCounter = tripForm.cleaned_data['tripItemCounter']        
        trip = tripForm.save( commit = False)

        trip.user = pRequest.user

        itemsSaved = False

        for i in range(0, tripItemCounter):
        
            itemSaved = False
            
            # TODO : ajouter un check if key exists (au cas où un item ait été supprimé)
            tripItemForm = TripItemForm( pRequest.POST, prefix = "TripItemForm" + str(i))
            print(pRequest.POST)
            print("TripItemForm" + str(i))
            print(tripItemForm)
            tripItemForm.trip = trip
            print(tripItemForm.is_valid())
            print(tripItemForm.errors)
        
            if tripItemForm.is_valid():
                tripItemForm.trip = trip
                print(tripItemForm)
                tripItemForm.save()
                itemSaved = True

            itemsSaved = itemsSaved and itemSaved 
        
        if itemsSaved:
            trip.save()


    return HttpResponseRedirect('/')