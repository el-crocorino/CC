from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from main_app.models import Trip, TripItem
from main_app.forms import TripForm, TripItemForm

@login_required
def trip_update( pRequest, pTripId):
    '''
    Trip udpate view
    @param int pTripId Trip id
    '''
    
    if pRequest.method == 'POST': 
        
        tripForm = TripForm( pRequest.POST, prefix = "TripForm")
        
        # save trip infos
        if tripForm.is_valid():

            trip = Trip.objects.get( id = pTripId)

            trip.date = tripForm.cleaned_data['date']
            trip.city_start = tripForm.cleaned_data['city_start']
            trip.city_end = tripForm.cleaned_data['city_end']
            trip.amount_limit = tripForm.cleaned_data['amount_limit']
            trip.participants_limit = tripForm.cleaned_data['participants_limit']
            trip.comment = tripForm.cleaned_data['comment']

            trip.save()

            tripItemCounter = tripForm.cleaned_data['tripItemCounter'] 
            itemsSaved = True
            tripItemIds = []

            #save trip items infos
            for i in range(0, tripItemCounter):

                itemSaved = False

                # check if data for given index exists in post query
                if pRequest.POST.get('TripItemForm' + str(i) + '-title', None) != None: 

                    tripItemForm = TripItemForm( pRequest.POST, prefix = "TripItemForm" + str(i))
                    tripItemForm.trip = trip
                
                    if tripItemForm.is_valid():

                        # if trip item already exists
                        if tripItemForm.cleaned_data['id'] != 'new':

                            tripItem = TripItem.objects.get( id = tripItemForm.cleaned_data['id'])
                            
                            tripItem.title = tripItemForm.cleaned_data['title']
                            tripItem.description = tripItemForm.cleaned_data['description']
                            tripItem.average_value = tripItemForm.cleaned_data['average_value']
                            tripItem.average_qty = tripItemForm.cleaned_data['average_qty']
                            tripItem.updated = datetime.now()
                            
                            tripItem.save()

                        # if new trip item
                        else:

                            tripItem = tripItemForm.save( commit = False)
                            tripItem.trip = trip
                            tripItem.save()

                            tripItemIds.append( tripItem.id)

                        itemSaved = True

                    itemsSaved = itemsSaved and itemSaved 
            
            # if error while saving trip items
            if not itemsSaved:

                trip.delete()

                for itemId in tripItemIds:
                    tripItem = TripItem.objects.get( id = itemId)
                    tripItem.delete()


            # Get trip infos form item diplay after updated
            trip.getOrders(pRequest.user.id)
            trip.getItems() 

            return render(pRequest, 'trip/item.html', {'trip': trip})

    else:

        trip = Trip.objects.get( id = pTripId)
        trip.items = TripItem.objects.filter( trip = pTripId)
        
        # set trip form
        updateTripForm = TripForm( prefix = 'TripForm',  initial = {
            'date' : trip.date, 
            'city_start' : trip.city_start, 
            'city_end' : trip.city_end, 
            'amount_limit' : trip.amount_limit, 
            'participants_limit' : trip.participants_limit, 
            'comment' : trip.comment
            })

        # set existing trip items forms
        updateTripItemForms = []
        
        for index, item in enumerate( trip.items, start = 0):
            
            updateTripItemForm = TripItemForm( prefix = 'TripItemForm' + str( index), initial = {
                'id' : item.id,
                'title': item.title,
                'description': item.description,
                'average_value': item.average_value,
                'average_qty': item.average_qty
            })

            updateTripItemForms.append( updateTripItemForm)
        
        #set new trip item form
        addTripItemForm = TripItemForm( prefix = 'TripItemForm')

        return render( pRequest, 'trip/update.html', {
            'trip': trip,
            'updateTripForm' : updateTripForm, 
            'addTripItemForm' : addTripItemForm, 
            'updateTripItemForms': updateTripItemForms
        }) 