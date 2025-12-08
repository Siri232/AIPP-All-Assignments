import requests
import json

# API Configuration
API_KEY = "e6c6083509fc4d450cde0ca4414b3a9f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch weather details for a city using OpenWeather API.
    Display weather details as JSON output.
    """
    # Parameters for API request
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    # Send GET request to API
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    
    # Parse JSON response
    data = response.json()
    
    # Display response as pretty JSON
    print(json.dumps(data, indent=4, ensure_ascii=False))
    
    return data

# Main program to get user input
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)

