import json
import sqlite3
from extractor import fetch_weather_data

DB_NAME = "weather.db"

def run_pipeline():
    print("Starting pipeline run...")
    
    # 1. EXTRACT
    raw_data = fetch_weather_data()
    if not raw_data:
        print("Pipeline failed at extraction step.")
        return
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 2. LOAD RAW STAGING DATA
    cursor.execute(
        "INSERT INTO raw_weather (raw_data) VALUES (?)",
        (json.dumps(raw_data),)
    )
    conn.commit()
    print("Raw JSON successfully landed in 'raw_weather' table.")
    
    # 3. TRANSFORM
    current = raw_data.get("current", {})
    recorded_at = current.get("time")
    temp = current.get("temperature_2m")
    humidity = current.get("relative_humidity_2m")
    wind_speed = current.get("wind_speed_10m")
    
    # Simple conditional logic for transformation
    condition = "Clear"
    if temp is not None and temp > 30:
        condition = "Hot"
    elif humidity is not None and humidity > 80:
        condition = "Humid / Rainy"
    
    # 4. LOAD CLEAN METRICS
    cursor.execute(
        """
        INSERT INTO clean_weather_metrics (recorded_at, temperature, humidity, wind_speed, weather_condition)
        VALUES (?, ?, ?, ?, ?)
        """,
        (recorded_at, temp, humidity, wind_speed, condition)
    )
    conn.commit()
    conn.close()
    
    print("Transformation complete! Clean data loaded into 'clean_weather_metrics'.")
    print(f"Recorded: {recorded_at} | Temp: {temp}°C | Humidity: {humidity}% | Condition: {condition}\n")

if __name__ == "__main__":
    run_pipeline()