# app/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess

def fetch_job():
    """Runs the fetch_data script as a subprocess."""
    print("⏳ Running scheduled fetch job...")
    subprocess.run(["python", "-m", "app.fetch_data"], check=True)
    print("✅ Fetch job completed.")

def start_scheduler():
    """Starts APScheduler with a daily cron job at 2 AM."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_job, "cron", hour=2, minute=0)  # Every day at 2:00 AM
    scheduler.start()
    print("🕒 Scheduler started (fetch_data will run daily at 2 AM)")
    return scheduler
