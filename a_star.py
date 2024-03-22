def a_star_algorithm(start, goal):
    open_nodes = set(start)
    closed_nodes = set()
    distances = {}  # store distance from start node
    parents = {}  # contains parent nodes for each node

    distances[start] = 0  # distance of start node from itself is 0
    parents[start] = start  # start node is its own parent

    while len(open_nodes) > 0:
        current_node = None

        # find node with lowest total cost (distance + heuristic)
        for node in open_nodes:
            if current_node is None or distances[node] + heuristic(node) < distances[current_node] + heuristic(current_node):
                current_node = node

        if current_node == goal or current_node not in graph:
            pass
        else:
            for neighbor, cost in get_neighbors(current_node):
                if neighbor not in open_nodes and neighbor not in closed_nodes:
                    open_nodes.add(neighbor)
                    parents[neighbor] = current_node
                    distances[neighbor] = distances[current_node] + cost
                else:
                    if distances[neighbor] > distances[current_node] + cost:
                        distances[neighbor] = distances[current_node] + cost
                        parents[neighbor] = current_node

                        if neighbor in closed_nodes:
                            closed_nodes.remove(neighbor)
                            open_nodes.add(neighbor)

        if current_node is None:
            print('Path does not exist!')
            return None

        if current_node == goal:
            path = []

            while parents[current_node] != current_node:
                path.append(current_node)
                current_node = parents[current_node]

            path.append(start)
            path.reverse()

            print('Path found:', path)
            return path

        open_nodes.remove(current_node)
        closed_nodes.add(current_node)

    print('Path does not exist!')
    return None

def get_neighbors(node):
    if node in graph:
        return graph[node]
    else:
        return None

def heuristic(node):
    return heuristic_distances[node]

def get_input():
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        node1, node2, cost = input("Enter node1 node2 cost: ").split()
        cost = int(cost)
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

    for node in graph:
        heuristic_value = int(input(f"Enter heuristic value for node {node}: "))
        heuristic_distances[node] = heuristic_value

# Describe your graph here
graph = {}
heuristic_distances = {}

if __name__ == "__main__":
    get_input()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    a_star_algorithm(start_node, goal_node)