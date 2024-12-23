from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'deadline', 'status', 'assigned_attendee', 'event']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
    }