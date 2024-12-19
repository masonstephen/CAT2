# events/filters.py
import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date', lookup_expr='exact')
    date_range = django_filters.DateFromToRangeFilter(field_name='date')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    venue = django_filters.CharFilter(field_name='venue__name', lookup_expr='icontains')
    organizer = django_filters.CharFilter(field_name='organizer__name', lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['date', 'date_range', 'title', 'venue', 'organizer']
