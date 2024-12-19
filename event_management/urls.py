from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.shortcuts import redirect
from events.views import CustomLoginView  # Import the custom login view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('accounts/login/', permanent=False)),  # Redirect to accounts login
    path('events/', include('events.urls')),  # Include the events app's URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Use custom login view
    path('accounts/', include('django.contrib.auth.urls')),
]
