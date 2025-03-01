import re

# Assign weights to different phishing keywords
PHISHING_KEYWORDS = {
    "urgent": 2, "verify": 3, "account": 2, "bank": 3, "password": 4,
    "login": 3, "click here": 3, "confirm": 2, "security alert": 3,
    "update your info": 4, "suspended": 5, "limited access": 3,
    "unauthorized": 4, "prize": 2, "winner": 2
}
def scan_emails():
    # Your phishing detection logic here
    pass

def detect_phishing_keywords(text):
    """Check if the text contains phishing keywords with a scoring system."""
    text = text.lower()  # Convert to lowercase for case-insensitive matching
    phishing_score = sum(weight for word, weight in PHISHING_KEYWORDS.items() if word in text)

    if phishing_score >= 10:
        return "High risk of phishing"
    elif phishing_score >= 5:
        return "Moderate risk of phishing"
    else:
        return "Low risk or safe"

# Example Usage
if __name__ == "__main__":
    email_texts = [
        "Dear user, your account has been suspended. Please update your info by clicking here.",
        "Congratulations! You are a winner. Click here to claim your prize.",
        "Your bank account is safe. No action is required."
    ]
    
    for email in email_texts:
        print(f"\nEmail: {email}")
        print(f"Risk Level: {detect_phishing_keywords(email)}")
