import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the distance from the start node to each node.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to keep track of nodes with the smallest tentative distance.
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip nodes that have already been visited.
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update the distance.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
