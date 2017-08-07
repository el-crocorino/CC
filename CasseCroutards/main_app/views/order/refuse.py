from django.http import HttpResponseRedirect
from datetime import datetime
from main_app.models import Order

def order_refuse( pRequest, pOrderId):

    order = Order.objects.get( id = pOrderId)

    if pRequest.method == 'POST':

        order.status = order.REFUSED
        order.updated = datetime.now()
    
        order.save()

        return HttpResponseRedirect('/trip/' + str(order.trip.id))

    else:
        