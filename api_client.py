import requests # type: ignore
from config.config import API_KEY, BASE_URL

def fetch_weather(city):
    params = {
        "q": f"{city['name']},{city['country']}",
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("API Error:", response.status_code)
        return None
