import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

DATABASE_PATH = "data/weather.db"
LOG_FILE = "logs/pipeline.log"

CITIES = [
    {"name": "Hyderabad", "country": "IN"},
    {"name": "Delhi", "country": "IN"},
    {"name": "Mumbai", "country": "IN"}
]

TEMP_MIN = -80
TEMP_MAX = 60
