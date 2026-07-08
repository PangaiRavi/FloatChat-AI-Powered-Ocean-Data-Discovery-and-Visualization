import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

LOCATIONS = {
    "Chennai": (13.0827, 80.2707),
    "Mumbai": (19.0760, 72.8777),
    "Kochi": (9.9312, 76.2673),
    "Goa": (15.2993, 74.1240),
    "Visakhapatnam": (17.6868, 83.2185),
    "Puducherry": (11.9416, 79.8083),
    "Mangalore": (12.9141, 74.8560),
    "Kanyakumari": (8.0883, 77.5385),
    "Tuticorin": (8.7642, 78.1348),
    "Paradip": (20.3167, 86.6167),
    "Puri": (19.8135, 85.8312),
    "Kollam": (8.8932, 76.6141),
    "Alappuzha": (9.4981, 76.3388),
    "Karwar": (14.8136, 74.1297),
    "Veraval": (20.9077, 70.3679)
}

OCEANS = {
    "Chennai": "Bay of Bengal",
    "Mumbai": "Arabian Sea",
    "Kochi": "Arabian Sea",
    "Goa": "Arabian Sea",
    "Visakhapatnam": "Bay of Bengal",
    "Puducherry": "Bay of Bengal",
    "Mangalore": "Arabian Sea",
    "Kanyakumari": "Indian Ocean",
    "Tuticorin": "Gulf of Mannar",
    "Paradip": "Bay of Bengal",
    "Puri": "Bay of Bengal",
    "Kollam": "Arabian Sea",
    "Alappuzha": "Arabian Sea",
    "Karwar": "Arabian Sea",
    "Veraval": "Arabian Sea"
}

def fetch_city_data(city, lat, lon):
    try:
        marine_url = (
            f"https://marine-api.open-meteo.com/v1/marine"
            f"?latitude={lat}"
            f"&longitude={lon}"
            f"&hourly=wave_height,sea_surface_temperature"
            f"&forecast_days=1"
        )

        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}"
            f"&longitude={lon}"
            f"&current=temperature_2m,wind_speed_10m"
        )

        marine = requests.get(marine_url, timeout=5).json()
        weather = requests.get(weather_url, timeout=5).json()

        return {
            "Date": marine["hourly"]["time"][0],
            "Location": city,
            "Ocean": OCEANS[city],
            "SST": marine["hourly"]["sea_surface_temperature"][0],
            "Salinity": 35.0,
            "WaveHeight": marine["hourly"]["wave_height"][0],
            "AirTemperature": weather["current"]["temperature_2m"],
	    "WindSpeed": weather["current"]["wind_speed_10m"]
        }
    except Exception as e:
        print(f"{city}: {e}")
        return None


def get_live_ocean_data():

    rows = []

    with ThreadPoolExecutor(max_workers=10) as executor:

        futures = []

        for city, (lat, lon) in LOCATIONS.items():
            futures.append(
                executor.submit(fetch_city_data, city, lat, lon)
            )

        for future in futures:
            result = future.result()

            if result:
                rows.append(result)

    df = pd.DataFrame(rows)

    print(df.head())
    print(df.columns.tolist())

    return df