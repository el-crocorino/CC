from django.shortcuts import render
from datetime import datetime

from main_app.models import Order
from main_app.forms import OrderForm

def order_update( pRequest, pOrderId):
    '''
    Order creation
    '''

    if pRequest.method == 'POST':

        orderForm = OrderForm( pRequest.POST)

        if orderForm.is_valid():

            order = Order.objects.get( id = pOrderId)

            order.comment = orderForm.cleaned_data['comment']
            order.amount = orderForm.cleaned_data['amount']
            order.updated = datetime.now()

            order.save()

            return render(pRequest, 'order/item.html', {'order': order, 'trip': order.trip})
    else:
        order = Order.objects.get( id = pOrderId)
        updateOrderForm = OrderForm( initial = {
            'comment' : order.comment, 
            'amount' : order.amount, 
            'user' : order.user, 
            'trip' : order.trip, 
            })
        
        return render(pRequest, 'order/update.html', {'order': order,'updateOrderForm' : updateOrderForm}) 