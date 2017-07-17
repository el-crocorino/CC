from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url( r'^user/new/$', views.user_create, name = 'trip add'),
    url( r'^user/profile/([0-9]+)/$', views.user_profile, name = 'trip add'), 

    url( r'^trip/([0-9]+)/$', views.trip_detail, name = 'trip detail'), 
    url( r'^trip/new/$', views.trip_create, name = 'trip add'), 
    url( r'^trip/delete/([0-9]+)$', views.trip_delete, name = 'trip delete'), 
    url( r'^trip/update/([0-9]+)$', views.trip_update, name = 'trip update'), 
    url( r'^$', views.index, name = 'index'), 
]