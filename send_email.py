import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv

# Constants
PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Load environment variables
current_dir = Path.cwd()

envars = current_dir / ".env"
print(envars)
load_dotenv(envars)

# Securely fetch credentials
sender_email = os.getenv("EMAIL")

password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    """Compose an email message."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["BCC"] = sender_email  # Optional: for internal tracking
    msg.set_content(
        f"""\
Hi {name},

I hope you are well.

I just wanted to drop you a quick note to remind you that {amount} USD with respect to our invoice {invoice_no} is due for payment on {due_date}.

I would be really grateful if you confirm that everything is on track for payment.

Best regards,
PLUM
"""
    )
    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
            server.starttls()
            server.login(str(sender_email),str( password_email))
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

    return msg

if __name__ == "__main__":
    # Compose the email
    email_message = send_email(
        subject="Invoice Reminder",
        receiver_email="i@gmail.com",
<<<<<<< HEAD
        name="k",
=======
        name="MEAWWW",
>>>>>>> 685062c (l)
        due_date="11, Aug 2022",
        invoice_no="INV-21-12-009",
        amount="5", 
    )

