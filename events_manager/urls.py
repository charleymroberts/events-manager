"""
URL configuration for events_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from events.views import show_dashboard, staff_events_list, add_event, add_performer, add_venue, edit_event, public_events_programme

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('all-events/', staff_events_list, name='all-events'),
    path('add-event/', add_event, name='add-event'),
    path('add-performer/', add_performer, name='add-performer'),
    path('add-venue/', add_venue, name='add-venue'),
    path('edit-event/<event_id>', edit_event, name='edit-event'),
    path('events-programme/', public_events_programme, name='events-programme')
]
