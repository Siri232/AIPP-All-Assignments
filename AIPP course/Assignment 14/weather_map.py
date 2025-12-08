import requests, json

api_key = "YOUR_API_KEY_HERE"  # Get free key from: https://openweathermap.org/api
city = input("City: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
print(json.dumps(requests.get(url).json(), indent=2))