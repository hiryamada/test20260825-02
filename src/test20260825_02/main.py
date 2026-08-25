import random

from fastapi import FastAPI

app = FastAPI(title="Weather Forecast API")

WEATHER_CONDITIONS = ["晴れ", "曇り", "雨", "雪", "晴れ時々曇り", "曇り時々雨"]


def generate_forecast(location: str) -> str:
    condition = random.choice(WEATHER_CONDITIONS)
    max_temp = random.randint(5, 40)
    min_temp = random.randint(0, max_temp - 1)
    return f"{location}の天気: {condition}、最高気温{max_temp}℃、最低気温{min_temp}℃"


@app.get("/weather/tokyo")
def get_weather_tokyo() -> dict:
    return {"forecast": generate_forecast("東京")}
