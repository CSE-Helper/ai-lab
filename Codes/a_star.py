from heapq import heappop, heappush


def astar_search(graph, heuristics, start, goal):
    open_list = [(0, start)]  # Priority queue of (f(n), node) tuples
    visited = set()
    g_scores = {start: 0}  # Cost from start along the best known path
    parent = {start: None}  # Parent nodes for each state

    while open_list:
        f, current_node = heappop(open_list)

        if current_node == goal:
            # Reached the goal state, build and return the optimal path
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path

        visited.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor in visited:
                continue

            g = g_scores[current_node] + cost
            h = heuristics[neighbor]
            f = g + h

            if neighbor not in g_scores or g < g_scores[neighbor]:
                # Found a better path to the neighbor, update the records
                heappush(open_list, (f, neighbor))
                g_scores[neighbor] = g
                parent[neighbor] = current_node

    # No path found
    return None


# Accept user input for the graph and heuristics
graph = {}
heuristics = {}

print("Enter the edges (format: 'node1-node2-cost'). Enter '$' to terminate.")
while True:
    edge = input("Enter an edge: ")
    if edge == "$":
        break

    node1, node2, cost = edge.split('-')
    cost = int(cost)

    if node1 not in graph:
        graph[node1] = {}
    graph[node1][node2] = cost

print("Enter the heuristic values (format: 'node-value'). Enter '$' to terminate.")
while True:
    heuristic = input("Enter a heuristic value: ")
    if heuristic == "$":
        break

    node, value = heuristic.split('-')
    value = int(value)

    heuristics[node] = value

# Accept user input for start and goal states
start_state = input("Enter the start state: ")
goal_state = input("Enter the goal state: ")

# Test the A* search algorithm
optimal_path = astar_search(graph, heuristics, start_state, goal_state)

if optimal_path:
    print("Optimal Path:", ' -> '.join(optimal_path))
else:
    print("No path found.")
