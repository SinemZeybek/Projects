import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

# Load .env variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")

def send_test_email():
    msg = EmailMessage()
    msg["Subject"] = "Flask Test Email"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg.set_content("This is a test email sent from your Flask app!")

    try:
        with smtplib.SMTP("smtp.googlemail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_test_email()
