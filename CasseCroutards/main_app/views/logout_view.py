
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def logout_view( pRequest):
    '''
    Logout
    '''
    logout( pRequest)
    return HttpResponseRedirect('/')