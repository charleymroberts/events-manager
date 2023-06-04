from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'date',
            'start_time',
            'end_time',
            'venue',
            'name',
            'type',
            'performers',
            'published'
        ]