from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            # print(f"Visiting: {node}")
            visited.append(node)
            if node == goal:
                print(f"✅ Found goal: {goal}")
                break
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    # print(f"  ➕ Adding {neighbor} to queue")
    print("\n🗺️ Visited Path:", visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

bfs(graph, start='A', goal='G')
