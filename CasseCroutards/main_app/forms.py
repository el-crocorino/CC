from django import forms
from .models import Trip
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
        
class LoginForm( forms.Form):
    email = forms.EmailField( label = 'E-Mail Address', max_length = 256)
    password = forms.CharField( widget = forms.PasswordInput())
    
    class Meta:
        app_label = 'main_app'

class TripForm( forms.ModelForm):
    class Meta:
        app_label = 'main_app'
        model = Trip
        fields = ['date', 'city_start', 'city_end', 'amount_limit', 'participants_limit', 'comment']

class SignUpForm( UserCreationForm):
    '''birth_date = forms.DateField( help_text = 'Format: YYYY-MM-DD')
    email = forms.EmailField( help_text = 'Required')'''

    class Meta:
        app_label = 'main_app'
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'birth_date', 'location', 'bio', 'avatar')

class UserUpdateForm( forms.ModelForm):

    class Meta:
        app_label = 'main_app'
        model = get_user_model()
        fields = ( 'location', 'bio', 'avatar')
