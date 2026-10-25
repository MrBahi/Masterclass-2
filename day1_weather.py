import requests

# 1. Open-Meteo endpoint targeting coordinates for Bujumbura, Burundi
url = "https://open-meteo.com"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # 2. Extract current weather metrics defensively from the JSON structure
    current = data.get("current", {})
    
    temp = current.get("temperature_2m")
    humidity = current.get("relative_humidity_2m")
    feels_like = current.get("apparent_temperature")
    wind = current.get("wind_speed_10m")
    
    # 3. Print a clean, human-readable summary with formatted numbers
    print("=" * 35)
    print(" LIVE WEATHER REPORT: BUJUMBURA ")
    print("=" * 35)
    print(f"Current Temperature : {temp}°C")
    print(f"Feels Like          : {feels_like}°C")
    print(f"Relative Humidity   : {humidity}%")
    print(f"Wind Speed          : {wind} km/h")
    print("=" * 35)
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")