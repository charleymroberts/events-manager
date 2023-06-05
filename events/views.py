from django.shortcuts import render, redirect
from .forms import EventForm, PerformerForm, VenueForm

# Create your views here.
def show_dashboard(request):
    return render(request, 'events/staff/dashboard.html')

def staff_events_list(request):
    return render(request, 'events/staff/all-events.html')

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

# add_event: page with custom form for adding events
# how do I actually implement edit/delete event?
# events_list to display all events so far