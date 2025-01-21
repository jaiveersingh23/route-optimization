def genetic_algorithm(distance_matrix, population_size=50, generations=100, mutation_rate=0.1):
    """
    Implements Genetic Algorithm for route optimization.
    """
    import random
    n = len(distance_matrix)

    # Generate initial population
    population = [random.sample(range(n), n) for _ in range(population_size)]

    def fitness(solution):
        return 1 / calculate_total_distance(distance_matrix, solution)

    for _ in range(generations):
        # Evaluate fitness
        fitness_scores = [fitness(individual) for individual in population]

        # Select parents
        parents = random.choices(
            population, weights=fitness_scores, k=population_size
        )

        # Crossover
        offspring = []
        for i in range(0, population_size, 2):
            p1, p2 = parents[i], parents[i + 1]
            cut = random.randint(1, n - 1)
            child = p1[:cut] + [gene for gene in p2 if gene not in p1[:cut]]
            offspring.append(child)

        # Mutate
        for child in offspring:
            if random.random() < mutation_rate:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]

        population = offspring

    best_solution = max(population, key=fitness)
    best_distance = calculate_total_distance(distance_matrix, best_solution)
    return best_solution, best_distance
def calculate_total_distance(distance_matrix, solution):
    return sum(
        distance_matrix[solution[i]][solution[i + 1]] for i in range(len(solution) - 1)
    ) + distance_matrix[solution[-1]][solution[0]]