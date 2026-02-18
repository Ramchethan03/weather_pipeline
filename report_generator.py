import pandas as pd
from database.db_manager import create_connection

def generate_report():
    conn = create_connection()

    query = """
        SELECT c.name, w.temperature, w.humidity,
               w.pressure, w.timestamp
        FROM weather w
        JOIN cities c ON w.city_id = c.id
    """

    df = pd.read_sql(query, conn)
    conn.close()

    print("\nWeather Report:\n")
    print(df)
