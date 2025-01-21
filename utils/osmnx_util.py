import osmnx as ox
import networkx as nx

def fetch_osm_distances(locations):
    """
    Generate a synthetic distance matrix using OSMNX.
    """
#    G = ox.graph_from_place("United States", network_type="drive")
    G = ox.graph_from_place("New York City, New York, USA", network_type="drive")

    def get_nearest_node(location):
        return ox.distance.nearest_nodes(G, location[1], location[0])

    nodes = [get_nearest_node(location) for location in locations]
    distances = []
    for i, origin in enumerate(nodes):
        row = []
        for j, destination in enumerate(nodes):
            if i != j:
                distance = nx.shortest_path_length(G, origin, destination, weight="length")
            else:
                distance = 0
            row.append(distance)
        distances.append(row)

    return distances
