from django.db import models
from event.models import Event  # Ensure Event model is imported

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField(Event, related_name='attendees')  # ManyToManyField to Event

    def _str_(self):
        return self.name 
