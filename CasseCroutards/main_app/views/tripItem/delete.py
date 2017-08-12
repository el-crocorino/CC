from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from main_app.models import TripItem

def tripItem_delete( pRequest):
    '''
    Trip item deletion
    '''
    tripItemId = pRequest.POST.get( 'itemId', None)
    responseMessage = ''

    if tripItemId and tripItemId != 'new':
    
        tripItem = TripItem.objects.get( id = tripItemId)
    
        if tripItem:
    
            title = tripItem.title
            tripItem.delete()
            responseMessage = title + ' ' + str( _("tripItemDeletion"))
    
        else : 
            responseMessage = title + ' ' + str( _("tripItemDeletionError"))
    
    return HttpResponse(responseMessage)