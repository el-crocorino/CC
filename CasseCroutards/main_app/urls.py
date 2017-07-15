from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url( r'^trip/([0-9]+)/$', views.trip_detail, name = 'trip detail'), 
    url( r'^trip/new/$', views.trip_add, name = 'trip add'), 
    url( r'^trip/delete/$', views.trip_delete, name = 'trip delete'), 
    url( r'^trip/update/$', views.trip_update, name = 'trip update'), 
    url( r'^$', views.index, name = 'index'), 
]