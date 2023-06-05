from django import forms
from .models import Event, Performer, Venue


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'date',
            'start_time',
            'end_time',
            'venue',
            'type',
            'name',
            'performers',
            'published'
        ]


class PerformerForm(forms.ModelForm):
    class Meta:
        model = Performer
        fields = [
            'name',
            'biog',
            'photo',
            'weblink'
        ]


class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = [
            'name',
            'location',
            'stepfree',
            'accessible_toilets'
        ]

