import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, weight))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0

        min_heap = [(0, start)]

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'A', 7)
    
    print(g.graph)

    start_vertex = 'A'
    shortest_distances = g.dijkstra(start_vertex)
    
    print(shortest_distances)
