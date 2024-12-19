# events/viewsets.py
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Organizer, Venue, Event, Attendee, Ticket, Review  # Added Review
from .serializers import OrganizerSerializer, VenueSerializer, EventSerializer, AttendeeSerializer, TicketSerializer, ReviewSerializer  # Added ReviewSerializer
from .filters import EventFilter

class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer
    permission_classes = [IsAuthenticated]

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = EventFilter
    search_fields = ['title', 'description', 'venue__name', 'organizer__name']
    ordering_fields = ['date', 'title', 'venue', 'organizer']

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [IsAuthenticated]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet): 
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer 
    permission_classes = [IsAuthenticated] 
    
    def perform_create(self, serializer): 
        serializer.save(user=self.request.user)
