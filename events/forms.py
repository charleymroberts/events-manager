from django import forms

from .models import Event, Performer, Venue


# Widgets code copied from Stack Overflow:
# https://stackoverflow.com/a/61081644/592139
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

        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),
            'start_time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'type': 'time'}
            ),
            'end_time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'type': 'time'}
            ),
        }


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
