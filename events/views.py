from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Venue, Performer
from .forms import EventForm, PerformerForm, VenueForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@permission_required("events.view_event")
def show_dashboard(request):
    return render(request, 'events/staff/dashboard.html')

@permission_required("events.view_event")
def staff_events_list(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/staff/all-events.html', context)


def public_events_programme(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'events/public/events-programme.html', context)


def view_performer(request, performer_id):
    performer = get_object_or_404(Performer, id=performer_id)
    context = {
        'performer': performer
    }
    return render(request, 'events/public/performer.html', context)


@permission_required("events.view_performer")
def list_all_performers(request):
    performers = Performer.objects.all()
    context = {
        'performers': performers
    }
    return render(request, 'events/staff/all-performers.html', context)


@permission_required("events.view_venue")
def list_all_venues(request):
    venues = Venue.objects.all()
    context = {
        'venues': venues
    }
    return render(request, 'events/staff/all-venues.html', context)


@permission_required("events.add_event")
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Event added successfully")
            return redirect('/all-events/')
    form = EventForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-event.html', context)


@permission_required("events.add_performer")
def add_performer(request):
    if request.method == 'POST':
        form = PerformerForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Performer added successfully")
            return redirect('/all-performers/')
    form = PerformerForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-performer.html', context)


@permission_required("events.add_venue")
def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Venue added successfully")
            return redirect('/all-venues/')
    form = VenueForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-venue.html', context)


@permission_required("events.change_event")
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event edited successfully")
            return redirect('/all-events/')
    form = EventForm(instance=event)
    context = {
        'form': form,
        'event': event
    }
    return render(request, 'events/staff/edit-event.html', context)


@permission_required("events.change_performer")
def edit_performer(request, performer_id):
    performer = get_object_or_404(Performer, id=performer_id)
    if request.method == 'POST':
        form = PerformerForm(request.POST, instance=performer)
        if form.is_valid():
            form.save()
            messages.success(request, "Performer edited successfully")
            return redirect('/all-performers/')
    form = PerformerForm(instance=performer)
    context = {
        'form': form,
        'performer': performer
    }
    return render(request, 'events/staff/edit-performer.html', context)


@permission_required("events.change_venue")
def edit_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            messages.success(request, "Venue edited successfully")
            return redirect('/all-venues/')
    form = VenueForm(instance=venue)
    context = {
        'form': form,
        'venue': venue
    }
    return render(request, 'events/staff/edit-venue.html', context)


@permission_required("events.delete_event")
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, "Event deleted")
    return redirect('/all-events/')


@permission_required("events.delete_performer")
def delete_performer(request, performer_id):
    performer = get_object_or_404(Performer, id=performer_id)
    performer.delete()
    messages.success(request, "Performer deleted")
    return redirect('/all-performers/')


@permission_required("events.delete_venue")
def delete_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    try:
        venue.delete()
        messages.success(request, "Venue deleted")
    except IntegrityError as error:
        messages.warning(request, "You cannot delete this venue because it has events assigned to it. You must delete or assign the events to a different venue before you can delete this venue.")
    return redirect('/all-venues/')