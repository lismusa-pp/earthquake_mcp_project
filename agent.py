import requests
from config import USGS_API_URL, MIN_MAGNITUDE

def fetch_earthquake_data():
    try:
        response = requests.get(USGS_API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[Agent] Failed to fetch data: {e}")
        return None

def filter_earthquakes(data, min_magnitude=MIN_MAGNITUDE):
    filtered = []
    for feature in data.get("features", []):
        props = feature["properties"]
        geom = feature["geometry"]

        magnitude = props.get("mag", 0)
        if magnitude is not None and magnitude >= min_magnitude:
            quake = {
                "time": props["time"],
                "place": props["place"],
                "magnitude": magnitude,
                "depth": geom["coordinates"][2],
                "url": props["url"]
            }
            filtered.append(quake)

    return filtered
