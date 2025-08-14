from fastapi import APIRouter, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

@router.get("/weather")
def get_weather(city: str):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error fetching weather data")
    
    data = response.json()
    forecast = []
    for item in data["list"][:7]:
        forecast.append({
            "date": item["dt_txt"],
            "temp": item["main"]["temp"],
            "description": item["weather"][0]["description"]
        })
    return {"city": city, "forecast": forecast}
