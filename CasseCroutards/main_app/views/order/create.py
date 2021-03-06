from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from main_app.forms import OrderForm
from main_app.models import Trip

@login_required
def order_create( pRequest, pTripId):
    '''
    Order creation view
    @param int pTripId Trip id
    '''

    orderTrip = Trip.objects.get( id = pTripId)

    if pRequest.method == 'POST':

        orderForm = OrderForm( pRequest.POST)

        if orderForm.is_valid():

            order = orderForm.save( commit = False)
            order.trip = orderTrip
            order.status = order.PENDING
            order.user = pRequest.user

            order.save()

            return HttpResponseRedirect('/order/' + str(order.id))
            
        else:
            return render(pRequest, 'order/create.html', {
            'orderForm' : orderForm, 
            'orderTrip': orderTrip
            }) 
    else:
        orderForm = OrderForm()     
        return render(pRequest, 'order/create.html', {
            'orderForm' : orderForm, 
            'orderTrip': orderTrip
            }) 