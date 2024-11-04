from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1, undirected=True):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        if undirected:
            self.graph[vertex2].append((vertex1, weight))  # For undirected graph

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(f'({v},{w})' for v, w in self.graph[vertex])}")

    # Shortest path using BFS for unweighted graphs
    def shortest_path_bfs(self, start_vertex, end_vertex):
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None
        visited = set()
        queue = deque([(start_vertex, [start_vertex])])
        
        while queue:
            current, path = queue.popleft()
            if current == end_vertex:
                return path
            visited.add(current)
            for neighbor, _ in self.graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
        return None

    # Detect cycle in the graph using DFS
    def has_cycle(self):
        visited = set()

        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, vertex):
                        return True
                elif parent != neighbor:
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

    # Dijkstra's algorithm for shortest path in a weighted graph
    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    # Check if the graph is bipartite
    def is_bipartite(self):
        color = {}

        for vertex in self.graph:
            if vertex not in color:
                queue = deque([vertex])
                color[vertex] = 0

                while queue:
                    current = queue.popleft()
                    for neighbor, _ in self.graph[current]:
                        if neighbor not in color:
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
        return True

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()

# Test Shortest Path using BFS
print("\nShortest path from 0 to 4:", g.shortest_path_bfs(0, 4))

# Test Cycle Detection
print("Does the graph have a cycle?", g.has_cycle())

# Test Dijkstra's Algorithm
print("\nShortest paths from vertex 0 using Dijkstra's algorithm:", g.dijkstra(0))

# Test if the graph is bipartite
print("\nIs the graph bipartite?", g.is_bipartite())
