import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
DB_NAME = "weather.db"

def get_latest_weather():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    cursor = conn.cursor()
    
    # Fetch the last 10 recorded metrics
    cursor.execute("SELECT * FROM clean_weather_metrics ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    weather_records = get_latest_weather()
    return render_template("index.html", records=weather_records)

if __name__ == "__main__":
    app.run(debug=True, port=5000)