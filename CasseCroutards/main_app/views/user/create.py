from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from main_app.forms import SignUpForm


def user_create( pRequest):
    '''
    User creation
    '''

    if pRequest.method == 'POST':
        
        user_form = SignUpForm( pRequest.POST)

        if user_form.is_valid():

            user = user_form.save()
            e = user_form.cleaned_data['email']
            p = user_form.cleaned_data['password1']

            user = authenticate( email = e, password = p)

            if user is not None:
                if user.is_active:
                    login( pRequest, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account is not active")
            else:
                print("Username and password don't match")

    else:
        user_form = SignUpForm()
    return render(pRequest, 'user/create.html', {
        'user_form': user_form
    })