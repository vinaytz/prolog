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
