from django.db import models
from attendive.models import Attendee
from event.models import Event

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]

    name = models.CharField(max_length=200)
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    assigned_attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='tasks')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tasks')

    def _str_(self):
        return self.name 
