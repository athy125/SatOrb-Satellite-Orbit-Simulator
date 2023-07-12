import requests
from datetime import datetime

def get_weather_forecast(location):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()

        for item in data.get("list", []):
            timestamp = item.get("dt")
            temperature = item.get("main", {}).get("temp")
            weather_description = item.get("weather", [{}])[0].get("description")
            weather_icon = item.get("weather", [{}])[0].get("icon")

            forecast_time = datetime.fromtimestamp(timestamp)

            yield {
                "time": forecast_time,
                "temperature": temperature,
                "description": weather_description,
                "icon": weather_icon
            }

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
