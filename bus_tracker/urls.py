from django.urls import path
from . import views

urlpatterns = [
    path('get_route/<int:start_id>/<int:end_id>/', views.get_optimized_route, name='get_optimized_route'),
]
