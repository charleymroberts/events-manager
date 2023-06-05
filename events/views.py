from django.shortcuts import render, redirect
from .forms import EventForm

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
            return redirect('staff_events_list')
    form = EventForm()
    context = {
        'form': form
    }
    return render(request, 'events/staff/add-event.html', context)


def add_performer(request):
    return render(request, 'events/staff/add-performer.html')


def add_venue(request):
    return render(request, 'events/staff/add-venue.html')

# add_event: page with custom form for adding events
# how do I actually implement edit/delete event?
# events_list to display all events so far