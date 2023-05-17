import random


def tsp_hill_climbing(cities, distances):
    current_solution = generate_random_solution(cities)
    current_cost = calculate_total_distance(current_solution, distances)

    while True:
        neighbors = get_neighbors(current_solution)
        best_neighbor = None
        best_cost = current_cost

        for neighbor in neighbors:
            neighbor_cost = calculate_total_distance(neighbor, distances)
            if neighbor_cost < best_cost:
                best_neighbor = neighbor
                best_cost = neighbor_cost

        if best_neighbor is None:
            break

        current_solution = best_neighbor
        current_cost = best_cost

    return current_solution, current_cost


def generate_random_solution(cities):
    solution = list(cities)
    random.shuffle(solution)
    return solution


def calculate_total_distance(solution, distances):
    total_distance = 0
    num_cities = len(solution)

    for i in range(num_cities):
        current_city = solution[i]
        # Wrap around to the first city
        next_city = solution[(i + 1) % num_cities]

        total_distance += distances[current_city][next_city]

    return total_distance


def get_neighbors(solution):
    neighbors = []
    num_cities = len(solution)

    for i in range(num_cities - 1):
        for j in range(i + 1, num_cities):
            neighbor = list(solution)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    return neighbors


# Example usage
cities = [1, 2, 3, 4]
distances = {
    1: {1: 0, 2: 10, 3: 15, 4: 20},
    2: {1: 10, 2: 0, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 3: 0, 4: 30},
    4: {1: 20, 2: 25, 3: 30, 4: 0}
}


solution, cost = tsp_hill_climbing(cities, distances)
print("Shortest route:", solution)
print("Total distance:", cost)
