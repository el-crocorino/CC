from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from .models import Trip
from .forms import TripForm, SignUpForm, LoginForm, UserUpdateForm
#from .forms import TripForm, UserProfileForm, SignUpForm, LoginForm

# Create your views here.
def index( pRequest):
    '''
    Homepage
    '''
    trips = Trip.objects.all
    addTripForm = TripForm
    return render(pRequest, 'index.html', {'trips': trips, 'addTripForm' : addTripForm})

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
                    return HttpResponseRedirect('/')
                else:
                    print("The account is not active")
            else:
                print("Username and password don't match")
    else :
        form = LoginForm()
        return render( pRequest, 'user/login.html', {'form': form})

def logout_view( pRequest):
    '''
    Logout
    '''
    logout( pRequest)
    return HttpResponseRedirect('/')

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
    return render(pRequest, 'user/user_create.html', {
        'user_form': user_form
    })

def user_profile( pRequest, pUserId):
    '''
    Detailed user view

    @param int pUserId User id
    '''
    user = get_user_model().objects.get( id = pUserId)
    return render(pRequest, 'user/profile.html', {'user': user})

def user_update( pRequest, pUserId):

    user = get_user_model().objects.get( id = pUserId)

    if pRequest.user.id == user.id:

        if pRequest.method == 'POST':

            userUpdateForm = UserUpdateForm( pRequest.POST)

            if userUpdateForm.is_valid():

                user.location = userUpdateForm.cleaned_data['location']
                user.bio = userUpdateForm.cleaned_data['bio']
                user.avatar = userUpdateForm.cleaned_data['avatar']
                user.save()
                return render(pRequest, 'user/profile.html', {'user': user})

        else :
            
            updateUserForm = UserUpdateForm( initial = {
                'location': user.location,
                'bio': user.bio,
                'avatar': user.avatar
                })
            return render( pRequest, 'user/profile_update.html', {'user' : user, 'updateUserForm': updateUserForm})
    else:
        return HttpResponseRedirect('/')

def user_delete( pRequest):
    pass

def trip_detail( pRequest, pTripId):
    '''
    Detailed trip view

    @param int pTripId Trip id
    '''
    trip = Trip.objects.get( id = pTripId)
    return render(pRequest, 'trip/trip_detail.html', {'trip': trip})
        
def trip_create( pRequest):

    form = TripForm( pRequest.POST)

    if form.is_valid():
        trip = form.save( commit = False)
        trip.user = pRequest.user
        trip.save()

    return HttpResponseRedirect('/')
        
def trip_delete( pRequest, pTripId):

    trip = Trip.objects.get( id = pTripId)
    trip.delete()

    return HttpResponseRedirect('/')
    
def trip_update( pRequest, pTripId):

    if pRequest.method == 'POST': 

        form = TripForm( pRequest.POST)

        if form.is_valid():
            trip = form.save( commit = False)
            trip.user = pRequest.user
            trip.save()
            return render(pRequest, 'trip/trip_detail.html', {'trip': trip})

    else:
        trip = Trip.objects.get( id = pTripId)
        updateTripForm = TripForm( initial = {
            'date' : trip.date, 
            'city_start' : trip.city_start, 
            'city_end' : trip.city_end, 
            'amount_limit' : trip.amount_limit, 
            'participants_limit' : trip.participants_limit, 
            'comment' : trip.comment
            })
        
        return render(pRequest, 'trip/trip_update.html', {'trip': trip,'updateTripForm' : updateTripForm}) 