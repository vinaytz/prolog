from queue import PriorityQueue

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))

    while not pq.empty():
        (h, node) = pq.get()
        print("Visiting:", node)
        if node == goal:
            print("Goal reached!")
            return

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    pq.put((heuristics[neighbor], neighbor))

# Graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Heuristics
heuristics = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0  # goal node
}

best_first_search(graph, heuristics, 'A', 'F')
