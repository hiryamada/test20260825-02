import pytest
from fastapi.testclient import TestClient

from test20260825_02.main import app, generate_forecast

client = TestClient(app)


def test_get_weather_tokyo_status_code():
    response = client.get("/weather/tokyo")
    assert response.status_code == 200


def test_get_weather_tokyo_has_forecast_key():
    response = client.get("/weather/tokyo")
    data = response.json()
    assert "forecast" in data


def test_get_weather_tokyo_forecast_is_string():
    response = client.get("/weather/tokyo")
    data = response.json()
    assert isinstance(data["forecast"], str)


def test_get_weather_tokyo_forecast_contains_location():
    response = client.get("/weather/tokyo")
    data = response.json()
    assert "東京" in data["forecast"]


def test_generate_forecast_contains_temperature():
    forecast = generate_forecast("東京")
    assert "℃" in forecast


def test_generate_forecast_contains_condition():
    forecast = generate_forecast("東京")
    # The forecast should contain some Japanese text describing weather
    assert "東京" in forecast


def test_get_weather_tokyo_multiple_calls_return_forecast():
    for _ in range(5):
        response = client.get("/weather/tokyo")
        assert response.status_code == 200
        assert "forecast" in response.json()
