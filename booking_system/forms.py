from django import forms
from .models import Booking, Services


class BookingForm(forms.ModelForm):
    """
    Form for booking appointments utilizing the Booking model.
    """
    class Meta:
        model = Booking
        fields = [
            'dog_name', 'dog_breed', 'service_name',
            'date_of_booking', 'appointment_time'
        ]
        widgets = {
            'date_of_booking': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }


class ServiceForm(forms.ModelForm):
    """
    Form for adding or editing services in the system, utilizing the 
    Services model.
    """
    class Meta:
        model = Services
        fields = ['service_name', 'cost', 'description', 'duration']
        widgets = {
            'service_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'duration': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'HH:MM:SS'}
            ),
        }
