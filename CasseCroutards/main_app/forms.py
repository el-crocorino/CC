from django import forms
from .models import Trip, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


'''
User Management Forms
'''

class LoginForm( forms.Form):
    email = forms.EmailField( label = 'E-Mail Address', max_length = 256)
    password = forms.CharField( widget = forms.PasswordInput())
    
    class Meta:
        app_label = 'main_app'

class SignUpForm( UserCreationForm):

    class Meta:
        app_label = 'main_app'
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'birth_date', 'location', 'bio', 'avatar')

class UserUpdateForm( forms.ModelForm):

    class Meta:
        app_label = 'main_app'
        model = get_user_model()
        fields = ( 'location', 'bio', 'avatar')

'''
Core Forms
'''

class TripForm( forms.ModelForm):
    class Meta:
        app_label = 'main_app'
        model = Trip
        fields = ['date', 'city_start', 'city_end', 'amount_limit', 'participants_limit', 'comment']

class OrderForm( forms.ModelForm):

    class Meta:
        app_label = 'main_app'
        model = Order
        fields = ( 'comment', 'amount')

class OrderDeleteForm( forms.Form):
    confirmation = forms.BooleanField( label = _('OrderDeleteCheckbox'))

    class Meta:
        app_label = 'main_app'
