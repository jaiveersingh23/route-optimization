import googlemaps
import pandas as pd

API_KEY = "YOUR_API_KEY"
gmaps = googlemaps.Client(key=API_KEY)

def fetch_distance_matrix(locations):
    """
    Fetch the distance matrix using Google Maps API.
    """
    distance_matrix = gmaps.distance_matrix(
        origins=locations,
        destinations=locations,
        mode="driving"
    )

    distances = []
    for i, origin in enumerate(locations):
        row = []
        for j, destination in enumerate(locations):
            distance = distance_matrix['rows'][i]['elements'][j]['distance']['value']  # Meters
            row.append(distance)
        distances.append(row)

    return distances
