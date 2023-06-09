from datetime import date, datetime

from django.contrib import admin
from django.urls import path, include, register_converter

from events import views


# Source: https://danjacob.net/posts/djangocustomconverters/
class DateConverter:
    regex = r"\d{4}-\d{1,2}-\d{1,2}"
    format = "%Y-%m-%d"

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: date) -> str:
        return value.strftime(self.format)


register_converter(DateConverter, "date")

urlpatterns = [
    # django admin panel
    path('admin/', admin.site.urls),

    # staff pages (login and permissions required)
    path('staff/dashboard/', views.show_dashboard, name='dashboard'),
    path('staff/all-events/', views.staff_events_list, name='all-events'),
    path('staff/all-performers/', views.list_all_performers,
         name='all-performers'),
    path('staff/all-venues/', views.list_all_venues, name='all-venues'),
    path('staff/add-event/', views.add_event, name='add-event'),
    path('staff/add-performer/', views.add_performer, name='add-performer'),
    path('staff/add-venue/', views.add_venue, name='add-venue'),
    path('staff/edit-event/<event_id>', views.edit_event, name='edit-event'),
    path('staff/edit-performer/<performer_id>', views.edit_performer,
         name='edit-performer'),
    path('staff/edit-venue/<venue_id>', views.edit_venue, name='edit-venue'),
    path('staff/delete-event/<event_id>', views.delete_event,
         name='delete-event'),
    path('staff/delete-performer/<performer_id>', views.delete_performer,
         name='delete-performer'),
    path('staff/delete-venue/<venue_id>', views.delete_venue,
         name='delete-venue'),
    path('events-programme/', views.public_events_programme,
         name='events-programme'),

    # public pages (no login required)
    path('', views.homepage, name='welcome'),
    path('performer/', views.view_by_performer, name='by-performer'),
    path('performer/<performer_id>', views.view_performer, name='performer'),
    path('venue/', views.view_by_venue, name='by-venue'),
    path('venue/<venue_id>', views.view_venue, name='venue'),
    path('day/', views.view_by_day, name='by-day'),
    path('day/<date:event_date>', views.events_on_day, name='events-on-day'),
    path('accounts/', include('allauth.urls')),
]
