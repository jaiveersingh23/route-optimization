from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time
import requests

def geocode_with_google(place, api_key):
    """Fallback geocoding using Google Maps API."""
    try:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={api_key}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            print(f"Google API error for {place}: {data['status']}")
            return None
    except Exception as e:
        print(f"Error with Google Geocoding API for {place}: {e}")
        return None

def geocode_locations(location_names, google_api_key=None):
    """Geocode locations using Nominatim with fallback to Google API."""
    geolocator = Nominatim(user_agent="geoapiExercises", timeout=10)
    locations = []

    for place in location_names:
        # Attempt Nominatim geocoding with retries
        retries = 1
        success = False
        for attempt in range(retries):
            try:
                location = geolocator.geocode(place)
                if location:
                    print(f"Nominatim geocoded {place}: ({location.latitude}, {location.longitude})")
                    locations.append((location.latitude, location.longitude))
                    success = True
                else:
                    print(f"Nominatim could not find {place}.")
                break
            except (GeocoderTimedOut, GeocoderServiceError) as e:
                print(f"Nominatim error for {place}: {e}. Retrying ({attempt + 1}/{retries})...")
                time.sleep(2 ** attempt)  # Exponential backoff
        if success:
            continue

        # Fallback to Google Geocoding API
        if google_api_key:
            fallback_location = geocode_with_google(place, google_api_key)
            if fallback_location:
                print(f"Google API geocoded {place}: {fallback_location}")
                locations.append(fallback_location)
            else:
                print(f"Failed to geocode {place} using Google API.")
        else:
            print(f"Failed to geocode {place}.")

    if not locations:
        print("Error: No valid locations found.")
        raise ValueError("Geocoding failed for all locations.")
    return locations
