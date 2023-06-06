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

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            form.save()
            # return redirect('dashboard/')
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
            # return redirect('dashboard/')
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
            # return redirect('dashboard/')
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
            # some kind of popup goes here to say edit successful?
            return redirect('/all-events/')
    form = EventForm(instance=event)
    context = {
        'form': form
    }
    return render(request, 'events/staff/edit-event.html', context)