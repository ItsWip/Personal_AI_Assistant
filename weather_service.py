import os
import requests

def get_weather(location):
    """
    Get current weather data for a specified location.
    
    Args:
        location (str): The city name or location to get weather for
        
    Returns:
        dict: Weather data including temperature, conditions, etc.
              or an error message if the request fails
    """
   
    api_key = os.environ.get("WEATHER_API_KEY")
    
    if not api_key:
        return {
            "error": "Weather API key is not configured. Please set the WEATHER_API_KEY environment variable."
        }
    
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    try:
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            weather_data = {
                "location": f"{data['name']}, {data.get('sys', {}).get('country', '')}",
                "temperature": round(data["main"]["temp"]),
                "feels_like": round(data["main"]["feels_like"]),
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "timestamp": data["dt"]
            }
            
            return weather_data
        else:
            error_data = response.json()
            error_message = error_data.get("message", "Unknown error")
            return {
                "error": f"Error fetching weather data: {error_message} (Status code: {response.status_code})"
            }
            
    except Exception as e:
        return {
            "error": f"Error connecting to weather service: {str(e)}"
        }
