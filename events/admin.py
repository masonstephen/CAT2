# events/admin.py
from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Event
from .models import Organizer

class EventAdmin(GuardedModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Organizer)
