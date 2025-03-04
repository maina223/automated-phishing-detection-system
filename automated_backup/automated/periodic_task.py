import schedule
import time
import os
from subprocess import call

# Function to run the scan_emails command
def scan_emails():
  os.system('python C:/Users/hp/OneDrive/Desktop/4.2/project/automated/manage.py scan_emails')

# Schedule the task to run every hour
schedule.every(1).hours.do(scan_emails)

# Keep the script running and checking the schedule
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 60 seconds before checking again
