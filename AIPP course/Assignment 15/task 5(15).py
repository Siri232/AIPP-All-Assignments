import os
import json
from typing import Optional, Dict

# Optional requests import; if missing we'll use mock/demo mode
try:
    import requests
except Exception:
    requests = None

# Mock data used when no API key is present (demo mode)
_MOCK = {
    "new york": {"city": "New York", "temp": 22, "humidity": 55, "weather": "Few clouds"},
    "london": {"city": "London", "temp": 18, "humidity": 60, "weather": "Clear sky"},
}


def _normalize(city: str) -> str:
    s = (city or "").strip()
    # remove surrounding single/double quotes if present
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1].strip()
    return s


def fetch_and_store(city: str, api_key: Optional[str] = None, path: str = "results.json") -> Optional[Dict]:
    """
    Fetch weather for `city`, print JSON result, and append it to `path`.
    Returns the dict on success or None on failure.
    """
    city_norm = _normalize(city)
    if not city_norm:
        print("Error: City name cannot be empty.")
        return None

    key = api_key or os.getenv("OWM_API_KEY")
    # Demo/mock mode when no API key or requests missing
    if not key or requests is None:
        data = _MOCK.get(city_norm.lower())
        if not data:
            print("Error: City not found. Please enter a valid city.")
            return None
    else:
        try:
            resp = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={"q": city_norm, "appid": key, "units": "metric"},
                timeout=6,
            )
            resp.raise_for_status()
            j = resp.json()
            main = j.get("main", {})
            if "temp" not in main or "humidity" not in main:
                print("Error: Unexpected API response format.")
                return None
            temp = int(round(float(main["temp"])))
            humidity = int(main["humidity"])
            weather = j.get("weather", [{}])[0].get("description", "").title()
            data = {"city": j.get("name", city_norm), "temp": temp, "humidity": humidity, "weather": weather}
        except requests.exceptions.HTTPError as e:
            code = getattr(e.response, "status_code", None)
            if code == 404:
                print("Error: City not found. Please enter a valid city.")
            elif code == 401:
                print("Error: Invalid API key.")
            else:
                print(f"Error: HTTP {code or 'unknown'}")
            return None
        except requests.exceptions.Timeout:
            print("Error: API request timed out.")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to API. Check your internet.")
            return None
        except Exception as e:
            print("Error:", e)
            return None

    # Print JSON output (user-friendly)
    print(json.dumps(data, indent=2))

    # Append to file safely
    arr = []
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf8") as f:
                try:
                    arr = json.load(f)
                    if not isinstance(arr, list):
                        arr = []
                except Exception:
                    arr = []
    except Exception:
        arr = []

    arr.append(data)
    with open(path, "w", encoding="utf8") as f:
        json.dump(arr, f, indent=2)

    return data


# --- 3 simple assert tests (use temporary file, uncomment to run) ---
def _run_tests():
    import tempfile

    # ensure demo/mock mode
    os.environ.pop("OWM_API_KEY", None)
    tf = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    tf.close()
    try:
        # Test 1: valid demo city New York
        res = fetch_and_store("New York", path=tf.name)
        assert isinstance(res, dict) and res.get("city") == "New York", "Test1 failed"

        # Test 2: invalid city returns None
        res2 = fetch_and_store("xyz123", path=tf.name)
        assert res2 is None, "Test2 failed"

        # Test 3: valid demo city London
        res3 = fetch_and_store('"London"', path=tf.name)  # input with quotes
        assert isinstance(res3, dict) and res3.get("city") == "London", "Test3 failed"

        # Quick check that file has New York and London entries
        with open(tf.name, "r", encoding="utf8") as f:
            arr = json.load(f)
            assert isinstance(arr, list) and any(x.get("city") == "New York" for x in arr), "File missing New York"
            assert any(x.get("city") == "London" for x in arr), "File missing London"

        print("All tests passed (demo/mock mode).")
    finally:
        try:
            os.remove(tf.name)
        except Exception:
            pass


if __name__ == "__main__":
    # Interactive run: prompt user, then fetch & store
    # To use the real API, set env var OWM_API_KEY first (PowerShell):
    # $env:OWM_API_KEY = 'your_real_openweathermap_key_here'
    inp = input("Enter city name: ")
    fetch_and_store(inp)
    # To run the tests uncomment below:
    # _run_tests()