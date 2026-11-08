from django import forms
from .models import Event, Guest, Ticket

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'capacity']

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['full_name', 'phone', 'guest_type']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'guest', 'price', 'is_paid']