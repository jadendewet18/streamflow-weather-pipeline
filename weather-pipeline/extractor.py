import requests

def fetch_weather_data():
    # Open-Meteo API for Stellenbosch/Cape Town coordinates
    url = "https://api.open-meteo.com/v1/forecast?latitude=-33.92&longitude=18.42&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raises an error for bad status codes (like 404 or 500)
        data = response.json()
        print("Successfully fetched live weather data!")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

if __name__ == "__main__":
    weather_json = fetch_weather_data()
    print(weather_json)