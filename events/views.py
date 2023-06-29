from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Venue, Performer
from .forms import EventForm, PerformerForm, VenueForm
from django.contrib.auth.decorators import login_required, permission_required


'''
Staff pages. Function names should (hopefully) be self-explanatory.
@login_required decorator = user has to sign up and create an account. 
@permissions_required decorator = user needs that specific permission granting by the superuser via the admin panel 
(i.e. access that will be granted to staff users by one of their team)
In a future version pages may be added for logged-in public users that will just need the @login_required decorator
'''


@login_required()
@permission_required("events.view_event", raise_exception=True)
def show_dashboard(request):
    return render(request, 'events/staff/dashboard.html')


@login_required()
@permission_required("events.view_event", raise_exception=True)
def staff_events_list(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/staff/all-events.html', context)


@login_required()
@permission_required("events.view_performer", raise_exception=True)
def list_all_performers(request):
    performers = Performer.objects.all()
    context = {
        'performers': performers
    }
    return render(request, 'events/staff/all-performers.html', context)


@login_required()
@permission_required("events.view_venue", raise_exception=True)
def list_all_venues(request):
    venues = Venue.objects.all()
    context = {
        'venues': venues
    }
    return render(request, 'events/staff/all-venues.html', context)


@login_required()
@permission_required("events.add_event", raise_exception=True)
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Event added successfully")
            return redirect('all-events')
    form = EventForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-event.html', context)


@login_required()
@permission_required("events.add_performer", raise_exception=True)
def add_performer(request):
    if request.method == 'POST':
        form = PerformerForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, "Performer added successfully")
            return redirect('all-performers')
    form = PerformerForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-performer.html', context)


@login_required()
@permission_required("events.add_venue", raise_exception=True)
def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Venue added successfully")
            return redirect('all-venues')
    form = VenueForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-venue.html', context)


@login_required()
@permission_required("events.change_event", raise_exception=True)
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event edited successfully")
            return redirect('all-events')
    form = EventForm(instance=event)
    context = {
        'form': form,
        'event': event
    }
    return render(request, 'events/staff/edit-event.html', context)


@login_required()
@permission_required("events.change_performer", raise_exception=True)
def edit_performer(request, performer_id):
    performer = get_object_or_404(Performer, id=performer_id)
    if request.method == 'POST':
        form = PerformerForm(request.POST, request.FILES, instance=performer)
        if form.is_valid():
            form.save()
            messages.success(request, "Performer edited successfully")
            return redirect('all-performers')
    form = PerformerForm(instance=performer)
    context = {
        'form': form,
        'performer': performer
    }
    return render(request, 'events/staff/edit-performer.html', context)


@login_required()
@permission_required("events.change_venue", raise_exception=True)
def edit_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            messages.success(request, "Venue edited successfully")
            return redirect('all-venues')
    form = VenueForm(instance=venue)
    context = {
        'form': form,
        'venue': venue
    }
    return render(request, 'events/staff/edit-venue.html', context)


@login_required()
@permission_required("events.delete_event", raise_exception=True)
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, "Event deleted")
    return redirect('all-events')


@login_required()
@permission_required("events.delete_performer", raise_exception=True)
def delete_performer(request, performer_id):
    performer = get_object_or_404(Performer, id=performer_id)
    performer.delete()
    messages.success(request, "Performer deleted")
    return redirect('all-performers')


@login_required()
@permission_required("events.delete_venue", raise_exception=True)
def delete_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    try:
        venue.delete()
        messages.success(request, "Venue deleted")
    except IntegrityError as error:
        messages.warning(request, "You cannot delete this venue because it has events assigned to it. You must delete or assign the events to a different venue before you can delete this venue.")
    return redirect('all-venues')


'''
Public pages (no login required to view these)
'''


def homepage(request):
    return render(request, 'events/public/welcome.html')


def public_events_programme(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'events/public/events-programme.html', context)


def view_by_performer(request):
    performers = Performer.objects.all()
    context = {
        'performers': performers
    }
    return render(request, 'events/public/by-performer.html', context)


def view_performer(request, performer_id):
    performer = get_object_or_404(Performer, id=performer_id)
    events = performer.event_set.all()
    context = {
        'performer': performer,
        'events': events
    }
    return render(request, 'events/public/performer.html', context)


def view_by_venue(request):
    venues = Venue.objects.all()
    context = {
        'venues': venues
    }
    return render(request, 'events/public/by-venue.html', context)


def view_venue(request, venue_id):
    this_venue = get_object_or_404(Venue, id=venue_id)
    events = Event.objects.filter(venue=this_venue)
    context = {
        'venue': this_venue,
        'events': events
    }
    return render(request, 'events/public/venue.html', context)


def view_by_day(request):
    days = Event.objects.dates("date", "day")
    context = {
        'days': days
    }
    return render(request, 'events/public/by-day.html', context)


def events_on_day(request, event_date):
    events = Event.objects.filter(date=event_date)
    days = Event.objects.dates("date", "day")
    context = {
        'events': events,
        'days': days,
        'event_date': event_date,
    }
    return render(request, 'events/public/day.html', context)