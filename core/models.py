from django.db import models
from django.core.mail import send_mail
from django.conf import settings

class EmailRecord(models.Model):
    sender = models.CharField(max_length=255)
    subject = models.TextField()
    is_phishing = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.is_phishing:
            send_mail(
                'Phishing Alert Detected!',
                f'Alert: A phishing email was detected from {self.sender} with subject "{self.subject}".',
                settings.EMAIL_HOST_USER,
                ['admin@example.com'],  # Change to actual recipients
                fail_silently=False,
            )
        super().save(*args, **kwargs)
