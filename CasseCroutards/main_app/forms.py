from django import forms
from .models import Trip, UserProfile

class TripForm( forms.ModelForm):
	class Meta:
		model = Trip
		fields = ['date', 'city_start', 'city_end', 'amount_limit', 'participants_limit', 'comment']

class UserProfileForm( forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['email', 'avatar']

