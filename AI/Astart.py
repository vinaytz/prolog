import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('C', 1), ('D', 4)],
    'C': [('D', 2)],
    'D': [('G', 5)],
    'G': []
}


heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'G': 0
}

def a_star(start, goal):
    # Priority Queue for paths with total cost = cost_so_far + heuristic
    queue = [(0 + heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        est_total_cost, cost_so_far, current_node, path = heapq.heappop(queue)

        # If goal is reached
        if current_node == goal:
            print("Goal reached! ✅")
            print("Path:", path)
            print("Total Cost:", cost_so_far)
            return

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                total_cost = cost_so_far + cost
                est = total_cost + heuristic[neighbor]
                heapq.heappush(queue, (est, total_cost, neighbor, path + [neighbor]))

    print("Goal not reachable ❌")

a_star('A', 'G')
