def reinforcement_learning(distance_matrix, episodes=500, gamma=0.9, alpha=0.1, epsilon=0.1):
    """
    Implements Deep Reinforcement Learning for route optimization using Q-Learning.
    """
    import numpy as np
    import random

    n = len(distance_matrix)

    # Initialize Q-table
    Q = np.zeros((n, n))

    def get_next_action(current_city, unvisited):
        if random.random() < epsilon:
            return random.choice(unvisited)
        else:
            q_values = [(Q[current_city][j], j) for j in unvisited]
            return max(q_values, key=lambda x: x[0])[1]

    def calculate_reward(route):
        return -calculate_total_distance(distance_matrix, route)

    best_solution = None
    best_distance = float("inf")

    for _ in range(episodes):
        unvisited = list(range(1, n))  # Start at city 0
        current_city = 0
        route = [current_city]

        while unvisited:
            next_city = get_next_action(current_city, unvisited)
            reward = -distance_matrix[current_city][next_city]
            best_future_q = max([Q[next_city][j] for j in range(n) if j != current_city])

            # Update Q-value
            Q[current_city][next_city] = Q[current_city][next_city] + alpha * (
                reward + gamma * best_future_q - Q[current_city][next_city]
            )

            current_city = next_city
            route.append(current_city)
            unvisited.remove(current_city)

        route.append(0)  # Return to the starting city
        total_distance = calculate_total_distance(distance_matrix, route)

        if total_distance < best_distance:
            best_distance = total_distance
            best_solution = route

    return best_solution, best_distance
def calculate_total_distance(distance_matrix, solution):
    return sum(
        distance_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1)
    ) + distance_matrix[solution[-1]][solution[0]]