import requests
from datetime import datetime

# sun = clear, rain = rain and drizzle, thunderstorm = thunderstorm, 
# clouds = cloudiness 

# Weather parameters
sun = 0 
rain = 0
snow = 0
thunderstorm = 0
clouds = 0
wind = 0
air_pressure = 0
temperature = 0
humidity = 0

# Settings for weather API call
latitude = 56.6616  # Example latitude for Kalmar
longitude = 16.3616  # Example longitude for Kalmar
api_key = "YOUR API KEY HERE" # Enter your own API key
units = "metric"

# Get the weather data from the API
def get_weather_data(lat, lon, api_key, units):
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}"
    
  try:
    response = requests.get(url)
    response.raise_for_status()
        
    weather_data = response.json()
    return weather_data
    
  except requests.exceptions.RequestException as e:
    print("Error:", e)
    return None

weather_data = get_weather_data(latitude, longitude, api_key, units)
if weather_data:
  for condition in weather_data['weather']:
    if condition['main'] == 'Clear':
      sun = 1
    elif condition['main'] == 'Rain' or condition['main'] == 'Drizzle':
      rain = 1
    elif condition['main'] == 'Snow':
      snow = 1
    elif condition['main'] == 'Thunderstorm':
      thunderstorm = 1

  clouds = weather_data['clouds']['all']

  wind = weather_data['wind']['speed']

  air_pressure = weather_data['main']['pressure']

  temperature = weather_data['main']['temp']

  humidity = weather_data['main']['humidity']

else:
  print("Failed to retrieve weather data.")

# Prepare data for POST request
data = {
    "timestamp": datetime.now().isoformat(),
    "sun": sun,
    "rain": rain,
    "snow": snow,
    "thunderstorm": thunderstorm,
    "clouds": clouds,
    "wind": wind,
    "air_pressure": air_pressure,
    "temperature": temperature,
    "humidity": humidity
}

# Token and headers for the API
TOKEN = "YOUR TOKEN HERE"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# API endpoint
api_endpoint = "YOUR ENDPOINT HERE"

#POST request
try:
    response = requests.post(api_endpoint, json=data, headers=headers)
    response.raise_for_status()
    print("Data posted successfully")
except requests.exceptions.RequestException as e:
    print("Error posting data:", e)
