import heapq
from django.http import JsonResponse
from .models import BusStop

# Example graph for bus stops
graph = {
    "Stop1": {"Stop2": 10, "Stop3": 15},
    "Stop2": {"Stop1": 10, "Stop3": 5, "Stop4": 10},
    "Stop3": {"Stop1": 15, "Stop2": 5, "Stop4": 5},
    "Stop4": {"Stop2": 10, "Stop3": 5}
}

def dijkstra(graph, start, end, skip_stops=[]):
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    path = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            if neighbor in skip_stops:
                continue

            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
                path[neighbor] = current_node

    # Rebuild the shortest path
    shortest_path = []
    current = end
    while current in path:
        shortest_path.insert(0, current)
        current = path[current]

    return shortest_path

def get_optimized_route(request, start_id, end_id):
    start_stop = BusStop.objects.get(id=start_id)
    end_stop = BusStop.objects.get(id=end_id)

    # Fetch all bus stops and determine which to skip (no passengers waiting)
    all_stops = BusStop.objects.all()
    skip_stops = [stop.name for stop in all_stops if not stop.passengers_waiting]

    # Get the optimized route
    optimized_route = dijkstra(graph, start_stop.name, end_stop.name, skip_stops)
    
    return JsonResponse({'optimized_route': optimized_route})
