from rest_framework import serializers
from .models import Organizer, Venue, Event, Attendee, Ticket
from django.contrib.auth.models import User 
from rest_framework import serializers
from rest_framework import serializers 
from .models import Organizer, Venue, Event, Attendee, Ticket
from .models import Event, Review

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = '__all__'

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields = ('id', 'username', 'password', 'email') 
        extra_kwargs = {'password': {'write_only': True}} 
    def create(self, validated_data): 
        user = User.objects.create_user(**validated_data) 
        return user

class OrganizerSerializer(serializers.ModelSerializer): 
    class Meta: model = Organizer 
    fields = '__all__' 
    
class VenueSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Venue 
        fields = '__all__' 
        
class EventSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Event 
        fields = '__all__' 
        
class AttendeeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Attendee 
        fields = '__all__' 

class TicketSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Ticket 
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Review 
        fields = '__all__'