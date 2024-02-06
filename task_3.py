import heapq

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        self.edges[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        self.edges[from_vertex].append((to_vertex, weight))

    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Приклад використання
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B", 1)
graph.add_edge("A", "C", 4)
graph.add_edge("B", "C", 2)
graph.add_edge("B", "D", 5)
graph.add_edge("C", "D", 1)

start_vertex = "A"
distances = graph.dijkstra(start_vertex)

for vertex, distance in distances.items():
    print(f"Найкоротший шлях від {start_vertex} до {vertex}: {distance}")
