from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from main_app.models import Order
from main_app.forms import OrderDeleteForm

@login_required
def order_delete( pRequest, pOrderId):
    '''
    Order deletion view
    @param int pOrderId Order id
    '''

    order = Order.objects.get( id = pOrderId)
    
    if pRequest.method == 'POST':
        
        orderDeleteForm = OrderDeleteForm( pRequest.POST)

        if orderDeleteForm.is_valid():
        
            if orderDeleteForm.cleaned_data['confirmation'] == True:
        
                order.delete()
                return HttpResponseRedirect('/')

            else:

                return render(pRequest, 'order/delete.html', {
                    'order': order, 
                    'orderDeleteForm' : orderDeleteForm, 
                    'showTripUser': True, 
                    'showTripOrder': False, 
                    'showOrderUser': False,
                    'showOrderTrip': False
                    }) 

    else:
        
        orderDeleteForm = OrderDeleteForm()

        return render(pRequest, 'order/delete.html', {
            'order': order, 
            'orderDeleteForm' : orderDeleteForm, 
            'showTripUser': True, 
            'showTripOrder': False, 
            'showOrderUser': False,
            'showOrderTrip': False
            }) 