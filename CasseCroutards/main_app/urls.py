from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url( r'^trip/([0-9]+)/$', views.trip_detail, name = 'trip detail'), 
    url( r'^$', views.index, name = 'index'), 
]