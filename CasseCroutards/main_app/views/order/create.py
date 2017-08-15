from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from main_app.forms import OrderForm, OrderItemForm
from main_app.models import Trip, OrderItem

@login_required
def order_create( pRequest, pTripId):
    '''
    Order creation view
    @param int pTripId Trip id
    '''

    orderTrip = Trip.objects.get( id = pTripId)
    orderTrip.getItems()

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

        orderForm = OrderForm( prefix = 'OrderForm')
        orderItemForms = []

        for tripItem in orderTrip.items:
        
            orderItemForm = OrderItemForm( {'tripItemId' : tripItem.id}, prefix = 'OrderItemForm' + str(tripItem.id))        
            orderItemForm.tripItem = tripItem        
            orderItemForms.append( orderItemForm)


        return render(pRequest, 'order/create.html', {
            'orderForm' : orderForm,
            'orderItemForms' : orderItemForms, 
            'orderTrip': orderTrip, 
            }) 