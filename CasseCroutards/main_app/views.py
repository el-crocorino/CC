from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Trip


# Create your views here.

def index(request):
    trips = Trip.objects.all
    return render(request, 'index.html', {'trips': trips})