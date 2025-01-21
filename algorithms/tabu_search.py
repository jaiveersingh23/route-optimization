def tabu_search(distance_matrix, iterations=100, tabu_size=10):
    """
    Implements Tabu Search for route optimization.
    """
    import random
    n = len(distance_matrix)

    # Generate an initial random solution
    current_solution = list(range(n))
    random.shuffle(current_solution)

    best_solution = current_solution[:]
    best_distance = calculate_total_distance(distance_matrix, best_solution)

    tabu_list = []

    for _ in range(iterations):
        neighbors = generate_neighbors(current_solution)
        candidate_solutions = [
            sol for sol in neighbors if sol not in tabu_list
        ]

        # Evaluate candidates
        for candidate in candidate_solutions:
            distance = calculate_total_distance(distance_matrix, candidate)
            if distance < best_distance:
                best_solution = candidate
                best_distance = distance
                tabu_list.append(candidate)
                if len(tabu_list) > tabu_size:
                    tabu_list.pop(0)

    return best_solution, best_distance

def generate_neighbors(solution):
    neighbors = []
    for i in range(len(solution) - 1):
        for j in range(i + 1, len(solution)):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def calculate_total_distance(distance_matrix, solution):
    return sum(
        distance_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1)
    ) + distance_matrix[solution[-1]][solution[0]]