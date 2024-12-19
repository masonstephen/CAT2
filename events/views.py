# events/views.py

import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
from django.http import HttpResponse
from django.contrib.auth.models import User, Group  # Import Group to manage user roles
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Event, Ticket, Organizer, Attendee
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import EventForm, UserRegistrationForm

def index(request):
    return HttpResponse("Welcome to the Event Management System API")

class CustomLoginView(LoginView):
    template_name = 'events/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User registered successfully.",
        }, status=status.HTTP_201_CREATED)

@login_required
def dashboard(request):
    # Redirect organizers to the organizer dashboard
    if request.user.is_staff or request.user.groups.filter(name='Organizer').exists():
        return redirect('organizer_dashboard')

    try:
        attendee = Attendee.objects.get(user=request.user)
        user_events = Ticket.objects.filter(attendee=attendee)
    except Attendee.DoesNotExist:
        user_events = Ticket.objects.none()

    context = {
        'events': user_events
    }

    return render(request, 'events/user_dashboard.html', context)

@login_required
def organizer_dashboard(request):
    events = Event.objects.all()
    return render(request, 'events/dashboard.html', {'events': events})

@login_required
@permission_required('events.can_edit_event', raise_exception=True)
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/edit_event.html', {'event': event})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            try:
                organizer = Organizer.objects.get(user=request.user)
                event.organizer = organizer
                event.save()
                return redirect('dashboard')
            except Organizer.DoesNotExist:
                form.add_error(None, "You must be an organizer to create an event.")
        else:
            print("Form errors:", form.errors)
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})

@login_required
def available_events(request):
    events = Event.objects.all()
    return render(request, 'events/available_events.html', {'events': events})

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    attendee, created = Attendee.objects.get_or_create(user=request.user)
    Ticket.objects.create(event=event, attendee=attendee, status='booked')
    return redirect('available_events')

@login_required
def purchase_ticket(request, event_id):
    event = Event.objects.get(id=event_id)
    Ticket.objects.create(event=event, attendee=request.user, ticket_type='Standard')
    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'events/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'events/register.html', {'form': form})
