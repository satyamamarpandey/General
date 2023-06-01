import requests
import json
from geonamescache import GeonamesCache

def fetch_weather_forecast(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for non-2xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the weather forecast: {e}")
        return None

def display_weather_forecast(city_name, weather_data):
    if weather_data is None:
        return

    print(f"Weather Forecast for {city_name}:")
    print("-" * 40)
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Weather Conditions: {weather_data['weather'][0]['description']}")
    print("-" * 40)

def main():
    # Load all countries, states, and cities
    gc = GeonamesCache()
    countries = gc.get_countries()
    states = gc.get_us_states()  # Use only US states for this example, modify as needed
    cities = gc.get_cities()

    # Prompt user for country
    country = input("Enter the country: ")

    # Prompt user for state
    state = input("Enter the state: ")

    # Prompt user for city
    city = input("Enter the city: ")

    # Construct full location name
    location = city
    if state:
        location += f", {state}"
    if country:
        location += f", {country}"

    api_key = "18b6528785f41ea32f9a2b424ac62bb4"
    weather_data = fetch_weather_forecast(location, api_key)
    display_weather_forecast(location, weather_data)

if __name__ == "__main__":
    main()
