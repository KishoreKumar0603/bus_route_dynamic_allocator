from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bus_tracker.urls')),  # Include the bus_tracker app's URLs
]
