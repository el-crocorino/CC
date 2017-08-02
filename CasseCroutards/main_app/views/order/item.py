from django.shortcuts import render

from main_app.models import Order, Trip


def order_item( pRequest, pOrderId):
    '''
    Order detailed view
    '''

    order = Order.objects.get( id = pOrderId)
    trip = Trip.objects.get( id = order.trip.id)

    return render(pRequest, 'order/item.html', {'order': order, 'trip': trip})