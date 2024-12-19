from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Event, Organizer, Venue, Ticket, Attendee

class EventTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.organizer = Organizer.objects.create(user=User.objects.create_user('testuser', 'test@example.com', 'testpass'))
        self.venue = Venue.objects.create(name='Test Venue')
        self.event_data = {
            'title': 'Test Event',
            'description': 'Test Description',
            'date': '2025-01-01T00:00:00Z',
            'organizer': self.organizer.id,
            'venue': self.venue.id
        }

    def test_create_event(self):
        response = self.client.post(reverse('event-list'), self.event_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_events(self):
        Event.objects.create(**self.event_data)
        response = self.client.get(reverse('event-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_event(self):
        event = Event.objects.create(**self.event_data)
        updated_data = self.event_data.copy()
        updated_data['title'] = 'Updated Test Event'
        response = self.client.put(reverse('event-detail', kwargs={'pk': event.id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_event(self):
        event = Event.objects.create(**self.event_data)
        response = self.client.delete(reverse('event-detail', kwargs={'pk': event.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
