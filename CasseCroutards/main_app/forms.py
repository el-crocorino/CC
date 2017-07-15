from django import forms
from .models import Trip

class TripForm( forms.ModelForm):
	class Meta:
		model = Trip
		fields = ['date', 'city_start', 'city_end', 'amount_limit', 'participants_limit', 'comment']

