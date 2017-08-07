from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from datetime import datetime
from main_app.models import Order

@login_required
def order_accept( pRequest, pOrderId):
    '''
    Order acceptation view
    @param int pOrderId Order id
    '''

    order = Order.objects.get( id = pOrderId)
    order.status = order.ACCEPTED
    order.updated = datetime.now()
    
    order.save()

    return HttpResponseRedirect('/trip/' + str(order.trip.id))