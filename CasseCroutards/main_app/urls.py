from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^login/$', views.login_view, name = 'login'),   
    url(r'^logout/$', views.logout_view, name = 'logout'),  

    url( r'^user/new/$', views.user_create, name = 'user_create'),
    url( r'^user/profile/([0-9]+)/$', views.user_profile, name = 'user_item'),
    url( r'^user/update/([0-9]+)/$', views.user_update, name = 'user_update'),

    url( r'^trip/([0-9]+)/$', views.trip_detail, name = 'trip_item'), 
    url( r'^trip/new/$', views.trip_create, name = 'trip_create'), 
    url( r'^trip/delete/([0-9]+)$', views.trip_delete, name = 'trip_delete'), 
    url( r'^trip/update/([0-9]+)$', views.trip_update, name = 'trip_update'), 

    url( r'^order/new/([0-9]+)/$', views.order_create, name = 'order_create'), 

    url( r'^$', views.index, name = 'index'), 
]