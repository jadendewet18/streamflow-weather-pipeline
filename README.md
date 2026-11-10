# StreamFlow: Full-Stack Automated Weather Data Pipeline

An end-to-end data pipeline and web application built with Python, SQLite, and Flask. StreamFlow extracts real-time weather data from an external API, stages raw payloads, transforms and loads clean metrics into a structured database, automates execution via background scheduling, and renders telemetry through a clean, minimalist web dashboard.

## Table of Contents

- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)

## System Architecture

1. **Extractor (`extractor.py`):** Connects to the Open-Meteo API with robust error handling to fetch live weather metrics for the Western Cape region.
2. **Database (`database.py`):** Initializes a local SQLite database (`weather.db`) with separate raw staging (`raw_weather`) and reporting (`clean_weather_metrics`) tables.
3. **Pipeline (`pipeline.py`):** Orchestrates the Extract, Load, Transform (ELT) cycle.
4. **Scheduler (`scheduler.py`):** Handles background automation and recurring job execution.
5. **Web Server (`app.py`):** A lightweight Flask application that queries the SQLite database to serve real-time metrics.
6. **Frontend Dashboard (`templates/index.html`):** A clean, flat-design operations dashboard featuring status badges and crisp typography.

## Project Structure

```text
weather-pipeline/
│
├── database.py         # SQLite schema initialization
├── extractor.py        # API extraction logic
├── pipeline.py         # Main ELT pipeline script
├── scheduler.py        # Background task runner
├── app.py              # Flask web server
├── templates/
│   └── index.html      # Dashboard UI
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Initialize the Database

```bash
python database.py
```

### 3. Run the Pipeline

Generate the initial records:

```bash
python pipeline.py
```

### 4. Launch the Web Dashboard

```bash
python app.py
```

Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the live interface.
