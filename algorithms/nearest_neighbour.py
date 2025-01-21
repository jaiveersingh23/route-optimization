def nearest_neighbor(distance_matrix):
    """
    Implements Nearest Neighbor Heuristic for route optimization.
    """
    n = len(distance_matrix)
    visited = [False] * n
    solution = [0]  # Start from the first city
    visited[0] = True

    for _ in range(n - 1):
        last = solution[-1]
        next_city = min(
            [(i, distance) for i, distance in enumerate(distance_matrix[last]) if not visited[i]],
            key=lambda x: x[1]
        )[0]
        solution.append(next_city)
        visited[next_city] = True

    solution.append(0)  # Return to the start
    total_distance = calculate_total_distance(distance_matrix, solution)
    return solution, total_distance
def calculate_total_distance(distance_matrix, solution):
    return sum(
        distance_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1)
    ) + distance_matrix[solution[-1]][solution[0]]