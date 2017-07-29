from django.shortcuts import render
from main_app.forms import OrderForm
from main_app.models import Trip

def order_create( pRequest, pTripId):
    '''
    Order creation
    '''

    if pRequest.method == 'POST':

        orderForm = OrderForm( pRequest.POST)

        if orderForm.is_valid():

            orderTrip = Trip.objects.get( id = pTripId)

            order = orderForm.save( commit = False)
            order.trip = orderTrip
            order.user = pRequest.user
            order.save()

            return render(pRequest, 'order/item.html', {'order': order, 'trip': orderTrip})
    else:
        orderForm = OrderForm()        
        return render(pRequest, 'order/create.html', {'orderForm' : orderForm}) 