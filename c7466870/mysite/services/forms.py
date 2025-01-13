from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', 'service','special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select a date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'placeholder': 'Select a time'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'special_requests': forms.Textarea(attrs={'placeholder': 'Any special requests?', 'rows': 3}),
        }