from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

from main_app.forms import  LoginForm


def login_view( pRequest):
    '''
    Login view
    '''
    if pRequest.method == 'POST':    

        form = LoginForm( pRequest.POST)

        if form.is_valid():

            u = form.cleaned_data['email']
            p = form.cleaned_data['password']

            user = authenticate( username = u, password = p)

            if user is not None:
                if user.is_active:
                    login( pRequest, user)
                    return HttpResponseRedirect( pRequest.POST.get('next','/accounts/profile/'))
                else:
                    print("The account is not active")
            else:
                print("Username and password don't match")
    else :
        form = LoginForm()
        return render( pRequest, 'user/login.html', {'form': form})