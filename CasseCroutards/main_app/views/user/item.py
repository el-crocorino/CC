from django.shortcuts import render
from django.contrib.auth import get_user_model

def user_item( pRequest, pUserId):
    '''
    Detailed user view

    @param int pUserId User id
    '''
    user = get_user_model().objects.get( id = pUserId)
    return render(pRequest, 'user/item.html', {'user': user})