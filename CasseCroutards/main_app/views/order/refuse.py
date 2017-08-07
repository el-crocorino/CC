from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from main_app.models import Order

def order_refuse( pRequest, pOrderId):

    order = Order.objects.get( id = pOrderId)

    if pRequest.method == 'POST':

        order.status = order.REFUSED
        order.updated = datetime.now()
    
        order.save()

        url = reverse('trip_item', kwargs = {'pTripId': order.trip.id})
        return HttpResponseRedirect( url)

    else:

        return render( pRequest, 'order/refuse.html', {'order' : order})