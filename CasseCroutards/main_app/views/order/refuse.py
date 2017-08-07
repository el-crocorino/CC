from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from datetime import datetime
from main_app.models import Order

@login_required
def order_refuse( pRequest, pOrderId):
    '''
    Order refusal view
    @param int pOrderId Order id
    '''

    order = Order.objects.get( id = pOrderId)

    if pRequest.method == 'POST':

        order.status = order.REFUSED
        order.updated = datetime.now()
    
        order.save()

        url = reverse('trip_item', kwargs = {'pTripId': order.trip.id})
        return HttpResponseRedirect( url)

    else:

        return render( pRequest, 'order/refuse.html', {'order' : order})