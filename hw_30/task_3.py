import os
import requests
from dotenv import load_dotenv

load_dotenv()


def display_weather(city: str, API_TOKEN: str) -> None:
    par = {"q": city, "appid": API_TOKEN, "units": "metric"}
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather", params=par
    )
    response_json = response.json()
    weather = response_json["weather"][0]["main"]
    temp = response_json["main"]["temp"]
    feel_like = response_json["main"]["feels_like"]
    temp_min = response_json["main"]["temp_min"]
    temp_max = response_json["main"]["temp_max"]
    wind = response_json["wind"]["speed"]
    print(
        f"""In the city {city} the weather is {weather}, now {temp}°C, with minimum temperature {temp_min}°C,
maximum temperature {temp_max}°C, felt as {feel_like}°C, with wind speed {wind} km/h."""
    )


city = input("Enter a city name: ")
display_weather(city, os.getenv("API_TOKEN"))
