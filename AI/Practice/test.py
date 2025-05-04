from queue import PriorityQueue  # Importing PriorityQueue for sorting based on heuristic value

# Define the Best First Search function
def best_first_search(graph, heuristics, start, goal):
    visited = set()  # Set to keep track of visited nodes
    pq = PriorityQueue()  # Priority queue to always pick node with lowest heuristic
    pq.put((heuristics[start], start))  # Insert the start node with its heuristic value
    # Loop until all nodes are explored or goal is found
    while not pq.empty():
        (h, node) = pq.get()  # Get the node with the lowest heuristic value
        print("Visiting:", node)
        

        if node == goal:  # If goal is found, stop
            print("Goal reached!")
            return

        if node not in visited:  # If not already visited
            visited.add(node)  # Mark as visited

            # For each neighbor of the current node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    # Add neighbor to queue with its heuristic value
                    pq.put((heuristics[neighbor], neighbor))


# Define the graph using adjacency list
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

best_first_search(graph, heuristics, 'A', 'F')  # Start from A and search for F