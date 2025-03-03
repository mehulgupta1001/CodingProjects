from fastapi import FastAPI, Query
import requests

app = FastAPI()

# API Endpoints
WHO_API_URL = "https://ghoapi.azureedge.net/api/"
GOOGLE_TRENDS_API = "https://trends.google.com/trends/api/explore"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
TWITTER_API_URL = "https://api.twitter.com/2/tweets/search/recent"

# Replace with actual API keys
WEATHER_API_KEY = "your_openweather_api_key"
TWITTER_BEARER_TOKEN = "your_twitter_bearer_token"

@app.get("/")
def home():
    return {"message": "Welcome to HealthTrend AI!"}

@app.get("/health_data")
def get_health_data(indicator: str = Query(..., title="WHO Indicator Code")):
    """ Fetches data from WHO API """
    try:
        response = requests.get(f"{WHO_API_URL}{indicator}")
        if response.status_code != 200:
            return {"error": f"WHO API returned {response.status_code}"}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.get("/weather")
def get_weather(city: str):
    """ Fetches weather data for a city """
    response = requests.get(f"{WEATHER_API_URL}?q={city}&appid={WEATHER_API_KEY}")
    return response.json()

@app.get("/twitter_trends")
def get_twitter_trends(query: str):
    """ Fetches health-related tweets """
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
    response = requests.get(f"{TWITTER_API_URL}?query={query}", headers=headers)
    return response.json()

