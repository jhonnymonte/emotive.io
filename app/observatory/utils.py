import os
import requests
from datetime import date, timedelta,datetime
import base64

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
ASTRONOMY_APPLICATION_ID = os.environ.get("ASTRONOMY_APPLICATION_ID")
ASTRONOMY_APPLICATION_SECRET = os.environ.get("ASTRONOMY_APPLICATION_SECRET")

def astronomy_api_token():
    application_id = ASTRONOMY_APPLICATION_ID
    application_secret = ASTRONOMY_APPLICATION_SECRET
    userpass=(f"{application_id}:{application_secret}")
    auth_string = base64.b64encode(userpass.encode()).decode()
    return auth_string

def get_weather_data(latitude, longitude):
    api_key = WEATHER_API_KEY # Reemplazar con tu clave de API
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch weather data"}
    

def get_sky_objects(latitude, longitude):
    current_time = datetime.now().strftime('%H:%M:%S')
    token = astronomy_api_token()
    url = "https://api.astronomyapi.com/api/v2/bodies/positions"
    headers = {
        "Authorization": f"Basic {token}"
    }
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "elevation": 0,
        "from_date": date.today(),
        "to_date": date.today() + timedelta(days=1),
        "time": current_time
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch sky objects data"}