from queue import PriorityQueue

def Befs(graph, heuristics, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))

    while not pq.empty():
        (h, node) = pq.get()
        print("Visiting Node: ", node)

        if node == goal:
            print("Goal Found!")
            return
        
        if node not in visited:
            visited.add(node)

            for neighour in graph[node]:
                if neighour not in visited:
                    pq.put((heuristics[neighour], neighour)) 

graph = {
    'A': ['B', 'C'],   # A connects to B and C
    'B': ['D', 'E'],   # B connects to D and E
    'C': ['F'],        # C connects to F
    'D': [],           # Leaf node
    'E': [],           # Leaf node
    'F': []            # Goal node
}

# Define heuristic values for each node (smaller means "closer" to goal)
heuristics = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0  # Goal node has 0
}


Befs(graph, heuristics, 'A', 'F')