import sqlite3

DB_NAME = "weather.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Table for raw JSON / ingested data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            raw_data TEXT
        )
    """)
    
    # Table for cleaned and transformed metrics
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clean_weather_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recorded_at TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            weather_condition TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database and tables initialized successfully!")

if __name__ == "__main__":
    init_db()