from django.shortcuts import render, get_object_or_404, redirect
from .models import Attendee
from .forms import AttendeeForm
from rest_framework import viewsets
from .models import Attendee
from .serializers import AttendeeSerializer

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
# List all attendees
def attendee_list(request):
    attendees = Attendee.objects.all()
    return render(request, 'attendee/attendee_list.html', {'attendees': attendees})

# Create a new attendee
def attendee_create(request):
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendee_list')
    else:
        form = AttendeeForm()
    return render(request, 'attendee/attendee_form.html', {'form': form})

# Edit an existing attendee
def attendee_edit(request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    if request.method == 'POST':
        form = AttendeeForm(request.POST, instance=attendee)
        if form.is_valid():
            form.save()
            return redirect('attendee_list')
    else:
        form = AttendeeForm(instance=attendee)
    return render(request, 'attendee/attendee_form.html', {'form': form})

# Delete an attendee
def attendee_delete(request, pk):
    attendee = get_object_or_404(Attendee, pk=pk)
    attendee.delete()
    return redirect('attendee_list')
    
