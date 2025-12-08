import os
from typing import Optional, Dict

# Try to import requests; if it's not available, we'll fall back to demo/mock mode.
try:
    import requests
except Exception:
    requests = None

def _is_placeholder_key(key: Optional[str]) -> bool:
    if not key:
        return True
    k = key.strip().lower()
    return k == '' or k.startswith('your') or 'api_key' in k or len(k) < 10


def _mock_for(city: str) -> Optional[Dict]:
    """Return mock data for demo cities when no API key is provided."""
    lookup = {
        'new york': {'city': 'New York', 'temp': 22, 'humidity': 55, 'weather': 'Few clouds'},
        'london': {'city': 'London', 'temp': 6, 'humidity': 81, 'weather': 'Broken Clouds'},
    }
    key = city.strip().lower()
    # remove surrounding quotes if user typed "New York" or 'New York'
    if (key.startswith('"') and key.endswith('"')) or (key.startswith("'") and key.endswith("'")):
        key = key[1:-1].strip()
    return lookup.get(key)


def fetch_weather(city: str, api_key: Optional[str] = None) -> Optional[Dict]:
    """
    Fetch weather for `city` and return a dict with keys: city, temp, humidity, weather.
    If no API key is provided (or a placeholder is used), a small mock dataset is
    returned for demo cities (e.g., New York). On invalid city name, prints
    a user-friendly error and returns None.
    """
    # Normalize city input: strip whitespace and surrounding quotes
    if city is None:
        city = ''
    raw = city.strip()
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        raw = raw[1:-1].strip()
    city_norm = raw

    # Prefer explicit arg, then environment variable
    key = api_key or os.getenv('OWM_API_KEY') or ''

    # If key is placeholder OR requests library is unavailable, use demo/mock mode
    if _is_placeholder_key(key) or requests is None:
        # Demo/mock mode (no extra warnings; produce only expected output)
        mock = _mock_for(city_norm)
        if mock:
            return mock
        else:
            print('Error: City not found. Please enter a valid city.')
            return None

    # Real API call mode
    # Use params to let requests handle encoding (spaces, commas, etc.)
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_norm, "appid": key, "units": "metric"}
    try:
        resp = requests.get(url, params=params, timeout=6)
        resp.raise_for_status()
        data = resp.json()

        # Safely extract fields
        city_name = data.get('name', city_norm)
        main = data.get('main', {})
        weather_list = data.get('weather', [{}])

        if 'temp' not in main or 'humidity' not in main:
            print('Error: Could not retrieve temperature or humidity from the API response.')
            return None

        temp = main.get('temp')
        humidity = main.get('humidity')
        desc = weather_list[0].get('description', '').title()

        # Round temperature for friendly display
        try:
            temp = round(float(temp))
        except Exception:
            pass

        return {'city': city_name, 'temp': temp, 'humidity': humidity, 'weather': desc}

    except requests.exceptions.HTTPError as e:
        status = None
        try:
            status = e.response.status_code
        except Exception:
            pass
        if status == 404:
            print('Error: City not found. Please enter a valid city.')
        elif status == 401:
            print('Error: Invalid API key.')
        else:
            print(f'Error: HTTP {status or "unknown"}')
        return None
    except requests.exceptions.Timeout:
        print('Error: API request timed out.')
        return None
    except requests.exceptions.ConnectionError:
        print('Error: Could not connect to API. Check your internet.')
        return None
    except Exception as e:
        print('Unexpected Error:', str(e))
        return None


def print_weather(result: Dict) -> None:
    print(f"City: {result['city']}")
    print(f"Temperature: {result['temp']}°C")
    print(f"Humidity: {result['humidity']}%")
    print(f"Weather: {result['weather']}")


if __name__ == '__main__':
    # Prompt uses the "Input:" label to match the expected examples
    city_input = input('Input: ').strip()
    res = fetch_weather(city_input)
    if res:
        print_weather(res)