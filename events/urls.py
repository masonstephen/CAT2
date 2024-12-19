# events/urls.py
from django.urls import path, include
from .views import index, RegisterView, dashboard, edit_event, create_event, purchase_ticket, available_events, book_event, register, CustomLoginView, organizer_dashboard
from rest_framework.routers import DefaultRouter
from .viewsets import OrganizerViewSet, VenueViewSet, EventViewSet, AttendeeViewSet, TicketViewSet, ReviewViewSet
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'organizers', OrganizerViewSet)
router.register(r'venues', VenueViewSet)
router.register(r'events', EventViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register_api'),
    path('dashboard/', dashboard, name='dashboard'),
    path('organizer_dashboard/', organizer_dashboard, name='organizer_dashboard'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('create_event/', create_event, name='create_event'),
    path('purchase_ticket/<int:event_id>/', purchase_ticket, name='purchase_ticket'),
    path('edit_event/<int:event_id>/', edit_event, name='edit_event'),
    
    # New URL patterns for user functionality
    path('available_events/', available_events, name='available_events'),
    path('book_event/<int:event_id>/', book_event, name='book_event'),
    path('register/', register, name='register'),
]
