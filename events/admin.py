from django.contrib import admin

from .models import Performer, Venue, Event

# Register your models here.

admin.site.register(Performer)
admin.site.register(Venue)
admin.site.register(Event)
