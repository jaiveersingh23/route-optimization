def ant_colony_optimization(distance_matrix, n_ants=10, n_iterations=100, alpha=1, beta=2, evaporation_rate=0.5):
    """
    Implements Ant Colony Optimization for route optimization.
    """
    import random
    import numpy as np
    n = len(distance_matrix)

    pheromone = np.ones((n, n))
    best_solution = None
    best_distance = float("inf")

    for _ in range(n_iterations):
        solutions = []
        distances = []

        for _ in range(n_ants):
            unvisited = list(range(n))
            solution = [unvisited.pop(random.randint(0, len(unvisited) - 1))]

            while unvisited:
                current = solution[-1]
                probabilities = [
                    (pheromone[current][j] ** alpha) * ((1 / distance_matrix[current][j]) ** beta)
                    for j in unvisited
                ]
                probabilities /= sum(probabilities)
                next_city = random.choices(unvisited, probabilities)[0]
                solution.append(next_city)
                unvisited.remove(next_city)

            solutions.append(solution)
            distances.append(calculate_total_distance(distance_matrix, solution))

        # Update pheromones
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1 - evaporation_rate)

        for solution, distance in zip(solutions, distances):
            for i in range(n - 1):
                pheromone[solution[i]][solution[i + 1]] += 1 / distance
            pheromone[solution[-1]][solution[0]] += 1 / distance

        min_distance = min(distances)
        if min_distance < best_distance:
            best_distance = min_distance
            best_solution = solutions[distances.index(min_distance)]

    return best_solution, best_distance
def calculate_total_distance(distance_matrix, solution):
    return sum(
        distance_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1)
    ) + distance_matrix[solution[-1]][solution[0]]