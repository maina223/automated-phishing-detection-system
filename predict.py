import pickle

# Load trained model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_phishing(email_text):
    """Predict whether an email is phishing or legitimate."""
    email_text = [email_text]  # Convert to list
    email_features = vectorizer.transform(email_text)  # Transform text to numerical form
    prediction = model.predict(email_features)[0]  # Predict using trained model
    return "Phishing" if prediction == 1 else "Legitimate"

# Example Usage
if __name__ == "__main__":
    email_text = "Congratulations! You have won a prize. Click here to claim now."
    print(predict_phishing(email_text))
