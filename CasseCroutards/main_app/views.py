from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

from .models import Trip
from .forms import TripForm, SignUpForm, LoginForm
#from .forms import TripForm, UserProfileForm, SignUpForm, LoginForm

# Create your views here.
def index( request):
    '''
    Homepage
    '''
    trips = Trip.objects.all
    addTripForm = TripForm
    return render(request, 'index.html', {'trips': trips, 'addTripForm' : addTripForm})

def login_view( request):
    '''
    Login view
    '''
    if request.method == 'POST':    
        form = LoginForm( request.POST)
        if form.is_valid():
            u = form.cleaned_data['email']
            p = form.cleaned_data['password']
            user = authenticate( username = u, password = p)
            if user is not None:
                if user.is_active:
                    login( request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account is not active")
            else:
                print("Username and password don't match")
    else :
        form = LoginForm()
        return render( request, 'user/login.html', {'form': form})

def logout_view( request):
    '''
    Logout
    '''
    print('Kikoo')
    logout( request)
    return HttpResponseRedirect('/')

def user_create( request):

    '''
    User creation
    '''

    if request.method == 'POST':
        
        user_form = SignUpForm( request.POST)
        #userProfile_form = UserProfileForm( request.POST)

        if user_form.is_valid():
        #if user_form.is_valid() and userProfile_form.is_valid():
            # TODO : update form handling to remove username field from form and use email instead
            user = user_form.save()
            #user.refresh_from_db()                                                          # This will load the Profile created by the Signal
            #userProfile_form = UserProfileForm( request.POST, instance = user.userprofile)  # Reload the profile form with the profile instance
            #userProfile_form.full_clean()                                                   # Manually clean the form. Implicitly called by "is_valid()" method
            #userProfile_form.save()                                                         # Save the form

            e = user_form.cleaned_data['email']
            p = user_form.cleaned_data['password1']
            user = authenticate( email = e, password = p)

            if user is not None:
                if user.is_active:
                    login( request, user)
                    return HttpResponseRedirect('/')

    else:
        user_form = SignUpForm()
        #userProfile_form = UserProfileForm()
    return render(request, 'user/user_create.html', {
        'user_form': user_form
    })
    '''return render(request, 'user/user_create.html', {
        'user_form': user_form,
        'userProfile_form': userProfile_form
    })'''

def trip_detail( request, tripId):
    '''
    Detailed trip view

    @param int tripId Trip id
    '''
    trip = Trip.objects.get(id = tripId)
    return render(request, 'trip/trip_detail.html', {'trip': trip})
        
def trip_create( request):

    form = TripForm( request.POST)

    if form.is_valid():
        trip = form.save( commit = False)
        trip.user = request.user
        trip.save()

    return HttpResponseRedirect('/')
        
def trip_delete( request, tripId):

    trip = Trip.objects.get( id = tripId)
    trip.delete()

    return HttpResponseRedirect('/')
        
def trip_update( request, tripId):

    trip = Trip.objects.get( id = tripId)
    addTripForm = TripForm( initial = {
        'date' : trip.date, 
        'city_start' : trip.city_start, 
        'city_end' : trip.city_end, 
        'amount_limit' : trip.amount_limit, 
        'participants_limit' : trip.participants_limit, 
        'comment' : trip.comment
        })
    
    return render(request, 'trip/trip_update.html', {'trip': trip,'addTripForm' : addTripForm})    