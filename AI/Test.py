from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node == goal:
                print("Goal: ", node)
                break
            for nabour in (graph[node]):
                if nabour not in visited:
                    queue.append(nabour)
    print("Visited: ", visited)

    
graph = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "D" : ["T", "H"],
    "H" : [],
    "E" : [],
    "C" : ["G"],
    "T" : []
}
bfs(graph, 'A', 'G')    
                    