from django.shortcuts import render

# Create your views here.
def show_dashboard(request):
    return render(request, 'events/staff/dashboard.html')

def staff_events_list(request):
    return render(request, 'events/staff/all-events.html')

def add_event(request):
    return render(request, 'events/staff/add-event.html')

# add_event: page with custom form for adding events
# how do I actually implement edit/delete event?
# events_list to display all events so far