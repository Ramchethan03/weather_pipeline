from database.db_manager import create_connection

def insert_city(name, country):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO cities (name, country)
        VALUES (?, ?)
    """, (name, country))

    conn.commit()

    cursor.execute("SELECT id FROM cities WHERE name = ?", (name,))
    city_id = cursor.fetchone()[0]

    conn.close()
    return city_id

def insert_weather(city_id, data):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weather (city_id, temperature, humidity,
        pressure, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        city_id,
        data["temperature"],
        data["humidity"],
        data["pressure"],
        data["latitude"],
        data["longitude"]
    ))

    conn.commit()
    conn.close()
