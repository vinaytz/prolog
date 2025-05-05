graph = {
    'A': [('B', 1), (['C', 'D'], 2)],
    'B': [('E', 1), ('F', 1)],
    'C': [('G', 1)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 2,
    'E': 0,
    'F': 0,
    'G': 0
}

solution_graph = {}

def AOStar(node):
    print("Expanding Node:", node)
    if node not in graph or not graph[node]:
        solution_graph[node] = []
        return heuristic[node]

    min_cost = float('inf')
    best_path = None

    for path in graph[node]:
        if isinstance(path[0], list):  # AND node
            cost = sum(heuristic[p] for p in path[0]) + path[1]
            if cost < min_cost:
                min_cost = cost
                best_path = path
        else:  # OR node
            cost = heuristic[path[0]] + path[1]
            if cost < min_cost:
                min_cost = cost
                best_path = [path[0]]

    solution_graph[node] = best_path if isinstance(best_path, list) else [best_path]
    
    for child in solution_graph[node]:
        AOStar(child)

    return min_cost

# Start the AO* algorithm
AOStar('A')
print("\nSolution Graph:", solution_graph)




# AO* Algorithm (AND-OR Graph based search)

# Graph structure: Node -> List of [child nodes] with cost
graph = {
    'A': [[('B', 'C'), 3], [('D',), 2]],
    'B': [[('E',), 1], [('F',), 4]],
    'C': [[('G',), 2]],
    'D': [[('H',), 3], [('I',), 6]],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}

# Heuristic values for each node
h = {
    'A': 6,
    'B': 2,
    'C': 4,
    'D': 3,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0
}

# Final solution path
solution = {}

# AO* algorithm definition
def ao_star(node, backtracking=False):
    print(f"Visiting node: {node}")

    # If the node has no children, it's a leaf node (end)
    if not graph[node]:
        solution[node] = []
        return h[node]

    min_cost = float('inf')   # To store minimum cost path
    best_path = None          # Best child group (could be AND or OR)
    
    # Loop through all possible children combinations
    for children, cost in graph[node]:
        total = 0
        for child in children:
            total += h[child]  # Add heuristics of all child nodes (AND nodes)
        total += cost          # Add edge cost

        # Find the group with minimum cost
        if total < min_cost:
            min_cost = total
            best_path = children

    # Update the solution path
    solution[node] = best_path
    h[node] = min_cost  # Update heuristic of current node

    # If not backtracking, recursively apply AO* on best children
    if not backtracking:
        for child in best_path:
            ao_star(child)

    return h[node]

# Starting AO* search from node A
ao_star('A')

# Print final solution path
print("\nOptimal Solution Path:")
for k in solution:
    print(f"{k} -> {solution[k]}")
