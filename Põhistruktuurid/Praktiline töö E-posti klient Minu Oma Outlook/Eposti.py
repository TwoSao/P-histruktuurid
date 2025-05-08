import smtplib
import ssl
from email.message import EmailMessage
from utils import clear_last_draft
def send_email_notification(to_email: str, subject: str, content: str):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "illyablagun@gmail.com"
    password = "aglz qocj cdzo llhx"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content(content)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(from_email, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")

    clear_last_draft()