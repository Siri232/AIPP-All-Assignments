import requests
import json

def get_weather_with_errors(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print("\n=== Weather Details ===")
        print(json.dumps(data, indent=4))
        return data
    except requests.exceptions.Timeout:
        print("Error: API request timed out. Please check your network connection.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your API key or network connection.")
    except requests.exceptions.HTTPError as e:
        error_msg = {
            401: "Error: Invalid API key. Please check your API key.",
            404: f"Error: City '{city}' not found. Please check the city name.",
            400: "Error: Invalid request. Please check your input."
        }.get(e.response.status_code, f"Error: HTTP {e.response.status_code} - Invalid city or API key.")
        print(error_msg)
    except json.JSONDecodeError:
        print("Error: Invalid response from API. Could not parse JSON.")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
    return None

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ").strip() or "YOUR_API_KEY"
    city = input("Enter city name: ").strip()
    if city:
        get_weather_with_errors(city, api_key)
    else:
        print("Error: City name cannot be empty.")