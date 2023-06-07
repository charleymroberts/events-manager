from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Venue, Performer
from .forms import EventForm, PerformerForm, VenueForm

# Create your views here.
def show_dashboard(request):
    return render(request, 'events/staff/dashboard.html')

def staff_events_list(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/staff/all-events.html', context)

def public_events_programme(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/public/events-programme.html', context)


def list_all_performers(request):
    performers = Performer.objects.all()
    context = {
        'performers': performers
    }
    return render(request, 'events/staff/all-performers.html', context)


def list_all_venues(request):
    venues = Venue.objects.all()
    context = {
        'venues': venues
    }
    return render(request, 'events/staff/all-venues.html', context)


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/all-events/')
    form = EventForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-event.html', context)


def add_performer(request):
    if request.method == 'POST':
        form = PerformerForm(request.POST)
        if form.is_valid:
            form.save()
    form = PerformerForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-performer.html', context)


def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/all-venues/')
    form = VenueForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-venue.html', context)


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/all-events/')
    form = EventForm(instance=event)
    context = {
        'form': form
    }
    return render(request, 'events/staff/edit-event.html', context)


def edit_performer(request, performer_id):
    performer = get_object_or_404(Performer, id=performer_id)
    if request.method == 'POST':
        form = PerformerForm(request.POST, instance=performer)
        if form.is_valid():
            form.save()
            return redirect('/all-performers/')
    form = PerformerForm(instance=performer)
    context = {
        'form': form
    }
    return render(request, 'events/staff/edit-performer.html', context)


def edit_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('/all-venues/')
    form = VenueForm(instance=venue)
    context = {
        'form': form
    }
    return render(request, 'events/staff/edit-venue.html', context)

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('/all-events/')


def delete_performer(request, performer_id):
    performer = get_object_or_404(Performer, id=performer_id)
    performer.delete()
    return redirect('/all-performers/')


def delete_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    venue.delete()
    return redirect('/all-venues/')