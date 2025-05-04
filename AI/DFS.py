def dfs(graph, start, goal):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                print("Found goal:", goal)
                break
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    print(neighbor)
    
    print("Visited:", visited)

    
graph = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "D" : ["T", "H"],
    "H" : [],
    "E" : [],
    "C" : ["G"],
    "T" : []
}
dfs(graph, 'A', 'G')
