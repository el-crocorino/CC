from django import forms
from .models import Trip
#from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
        
class LoginForm( forms.Form):
    username = forms.CharField( label = 'User name', max_length = 64)
    password = forms.CharField( widget = forms.PasswordInput())

class TripForm( forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['date', 'city_start', 'city_end', 'amount_limit', 'participants_limit', 'comment']

'''class UserProfileForm( forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['location', 'bio', 'avatar']'''


class SignUpForm( UserCreationForm):
    birth_date = forms.DateField( help_text = 'Format: YYYY-MM-DD')
    email = forms.EmailField( help_text = 'Required')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'birth_date')
