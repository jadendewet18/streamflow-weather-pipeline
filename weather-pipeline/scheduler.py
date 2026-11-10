import time
import schedule
from pipeline import run_pipeline

def job():
    print("\n--- Scheduled Pipeline Triggered ---")
    try:
        run_pipeline()
    except Exception as e:
        print(f"Pipeline encountered an error during execution: {e}")

# Schedule the job to run every 10 seconds for testing (change to every().day.at("06:00") for production daily runs)
schedule.every(10).seconds.do(job)

print("Pipeline scheduler is running... Press Ctrl+C to exit.")

# Run an initial run immediately upon starting
job()

# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)