# bus_route/urls.py
from django.contrib import admin
from django.urls import path
from bus_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ensure this maps to your view
]
