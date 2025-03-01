from django_cron import CronJobBase, Schedule
from phishing_detection.phishing_utils import detect_phishing_keywords

class ScanEmailsCronJob(CronJobBase):
    RUN_EVERY_MINS = 60  # Set interval (e.g., run every 60 minutes)

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'phishing_detection.scan_emails_cron'  # Unique code for your cron job

    def do(self):
        # Sample emails for scanning (Replace with actual email fetching logic)
        emails = [
            "Dear user, your account has been suspended. Please update your info by clicking here.",
            "Congratulations! You are a winner. Click here to claim your prize.",
            "Your bank account is safe. No action is required."
        ]
        
        for email in emails:
            result = detect_phishing_keywords(email)
            print(f"Email: {email}\nRisk Level: {result}\n")

        print("Email scanning completed.")

from django_cron import CronJobBase, Schedule
from phishing_detection.phishing_utils import detect_phishing_keywords

class ScanEmailsCronJob(CronJobBase):
    RUN_EVERY_MINS = 60  # Set interval (e.g., run every 60 minutes)

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'phishing_detection.scan_emails_cron'  # Unique code for your cron job

    def do(self):
        # Example emails (Replace with actual email fetching logic)
        emails = [
            "Dear user, your account has been suspended. Please update your info by clicking here.",
            "Congratulations! You are a winner. Click here to claim your prize.",
            "Your bank account is safe. No action is required."
        ]
        
        for email in emails:
            result = detect_phishing_keywords(email)
            print(f"Email: {email}\nRisk Level: {result}\n")

        print("Email scanning completed.")
