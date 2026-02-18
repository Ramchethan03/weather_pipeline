from config.config import TEMP_MIN, TEMP_MAX

def transform_data(raw):
    if not raw:
        return None

    temp = raw["main"]["temp"]

    if not (TEMP_MIN <= temp <= TEMP_MAX):
        return None

    return {
        "temperature": temp,
        "humidity": raw["main"]["humidity"],
        "pressure": raw["main"]["pressure"],
        "latitude": raw["coord"]["lat"],
        "longitude": raw["coord"]["lon"]
    }
