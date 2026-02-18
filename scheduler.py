import schedule
import time
from main import run_pipeline

def start_scheduler():
    schedule.every(1).hours.do(run_pipeline)

    while True:
        schedule.run_pending()
        time.sleep(1)
