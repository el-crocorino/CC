from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from main_app.models import TripItem
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
        
        trip.save()

        itemsSaved = True
        tripItemIds = []

        for i in range(0, tripItemCounter):
        
            itemSaved = False

            if pRequest.POST.get('TripItemForm' + str(i) + '-title', None) != None: 

                tripItemForm = TripItemForm( pRequest.POST, prefix = "TripItemForm" + str(i))
                tripItemForm.trip = trip
            
                if tripItemForm.is_valid():

                    tripItem = tripItemForm.save( commit = False)
                    tripItem.trip = trip
                    tripItem.save()

                    tripItemIds.append( tripItem.id)

                    itemSaved = True

                itemsSaved = itemsSaved and itemSaved 
        
        if not itemsSaved:

            trip.delete()

            for itemId in tripItemIds:
                tripItem = TripItem.objects.get( id = itemId)
                tripItem.delete()


    return HttpResponseRedirect('/')