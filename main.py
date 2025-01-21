import pandas as pd
from utils.google_maps_api import fetch_distance_matrix
from utils.osmnx_util import fetch_osm_distances
from algorithms.tabu_search import tabu_search
from algorithms.genetic_algorithm import genetic_algorithm
from algorithms.ant_colony import ant_colony_optimization
from algorithms.reinforcement_learning import reinforcement_learning
from algorithms.nearest_neighbour import nearest_neighbor
from visualization import plot_results
from utils.geocoding import geocode_locations

def main():
    # Load delivery locations
    location_names = pd.read_csv("data/locations.csv")["Location"].tolist()
    print(location_names)
    location_names = ['Manhattan, New York, NY', 'Brooklyn, New York, NY', 
                      'Queens, New York, NY', 'Bronx, New York, NY', 
                      'Staten Island, New York, NY']

    # Provide your Google Geocoding API Key here
    google_api_key = "YOUR_API_KEY"

    # Geocode locations
    print("Geocoding locations...")
    try:
        locations = geocode_locations(location_names, google_api_key)
    except ValueError as e:
        print(e)
        return

    print(f"Geocoded locations: {locations}")

    # Fetch distances using OpenStreetMap
    print("Fetching distances using OpenStreetMap...")
    osm_distances = fetch_osm_distances(locations)

    # Fetch distances using Google Maps API
    print("Fetching distances using Google Maps API...")
    google_distances = fetch_distance_matrix(locations)
    # Algorithm Results
    results = []

    # Tabu Search
    print("Running Tabu Search...")
    tabu_solution, tabu_distance = tabu_search(google_distances)
    results.append({"algorithm": "Tabu Search", "distance": tabu_distance})

    # Genetic Algorithm
    print("Running Genetic Algorithm...")
    ga_solution, ga_distance = genetic_algorithm(google_distances)
    results.append({"algorithm": "Genetic Algorithm", "distance": ga_distance})

    # Ant Colony Optimization
    print("Running Ant Colony Optimization...")
    ant_solution, ant_distance = ant_colony_optimization(google_distances)
    results.append({"algorithm": "Ant Colony", "distance": ant_distance})

    # Nearest Neighbor
    print("Running Nearest Neighbor Heuristic...")
    nn_solution, nn_distance = nearest_neighbor(google_distances)
    results.append({"algorithm": "Nearest Neighbor", "distance": nn_distance})

    # Reinforcement Learning
    print("Running Deep Reinforcement Learning...")
    rl_solution, rl_distance = reinforcement_learning(google_distances)
    results.append({"algorithm": "Reinforcement Learning", "distance": rl_distance})
    # Save Results to CSV
    pd.DataFrame(results).to_csv("results/comparison_results.csv", index=False)
    print("Results saved to results/comparison_results.csv")

    # Plot Results
    print("Plotting results...")
    plot_results(results)

if __name__ == "__main__":
    main()