from django import forms
from .models import Attendee

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'events']
        widgets = {
            'events': forms.CheckboxSelectMultiple(),
}