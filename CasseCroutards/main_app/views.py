from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Trip
from .forms import TripForm, SignUpForm, LoginForm
#from .forms import TripForm, UserProfileForm, SignUpForm, LoginForm

# Create your views here.
def index( request):
    trips = Trip.objects.all
    addTripForm = TripForm
    return render(request, 'index.html', {'trips': trips, 'addTripForm' : addTripForm})

def login_view( request):
    if request.method == 'POST':    
        form = LoginForm( request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
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
    print('Kikoo')
    logout( request)
    return HttpResponseRedirect('/')    

def trip_detail( request, tripId):
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