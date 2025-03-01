from django.core.management.base import BaseCommand
from phishing_detection import scan_emails  # Import your phishing scan function

class Command(BaseCommand):
    help = 'Scans emails for phishing content'

    def handle(self, *args, **kwargs):
        scan_emails()
        self.stdout.write("Scan completed successfully!")
