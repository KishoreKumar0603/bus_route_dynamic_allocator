from django.shortcuts import render
from .models import BusStop

def index(request):
    return render(request, 'index.html')

def get_optimized_route(request, start_id, end_id):
    start = BusStop.objects.get(id=start_id)
    end = BusStop.objects.get(id=end_id)
    # Placeholder logic for route optimization
    route = [start, end]
    return render(request, 'index.html', {'route': route})
