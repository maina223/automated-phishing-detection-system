import imaplib
import email
from email.header import decode_header
import os
import re

# IMAP Server Configuration
IMAP_SERVER = 'imap.gmail.com'  # Change for your email provider
IMAP_PORT = 993
EMAIL_USER = 'mariana@gmail.com'
EMAIL_PASS = '123456'

def connect_imap():
    """Connect to the IMAP server and log in."""
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("inbox")  # Select inbox
    return mail

def decode_mime_words(encoded_str):
    """Decode MIME words (e.g., subject or sender) in email headers."""
    decoded_words, encoding = decode_header(encoded_str)[0]
    if isinstance(decoded_words, bytes):
        return decoded_words.decode(encoding or 'utf-8')
    return decoded_words

def detect_phishing(body, sender):
    """Basic phishing detection using regex and keywords."""
    phishing_keywords = ['urgent action', 'verify your account', 'account suspension', 'immediate action required']
    suspicious_urls = ['bit.ly', 'goo.gl', 'paypal.com.secure']

    # Check for suspicious keywords in email body
    if any(keyword in body.lower() for keyword in phishing_keywords):
        return True

    # Check for suspicious sender domain
    if 'suspiciousdomain.com' in sender.lower():
        return True

    # Check for suspicious URLs
    if any(url in body for url in suspicious_urls):
        return True

    return False

def fetch_emails():
    """Fetch emails, parse them, and check for phishing."""
    mail = connect_imap()
    status, messages = mail.search(None, 'UNSEEN')  # Search for unread emails

    for num in messages[0].split():
        status, msg_data = mail.fetch(num, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # Decode subject and sender
                subject = decode_mime_words(msg["Subject"])
                sender = msg.get("From")

                # Extract email body
                body = ""
                if msg.is_multipart():
                    for part in msg.iter_parts():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        # Extract plain text body
                        if "attachment" not in content_disposition and "text/plain" in content_type:
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()

                # Check for phishing
                if detect_phishing(body, sender):
                    print(f"Phishing email detected from {sender} with subject: {subject}")
                else:
                    print(f"Safe email from {sender} with subject: {subject}")

    mail.logout()

# Run the email fetch and phishing detection
fetch_emails()
