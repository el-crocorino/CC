from django.http import HttpResponseRedirect
from datetime import datetime
from main_app.models import Order

def order_accept( pRequest, pOrderId):

    order = Order.objects.get( id = pOrderId)
    order.status = order.ACCEPTED
    order.updated = datetime.now()
    
    order.save()

    return HttpResponseRedirect('/trip/' + str(order.trip.id))