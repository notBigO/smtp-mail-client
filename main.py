import os
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from config.config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_email(to_address, subject, body, filename=None):
    try:
        # Set up the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.ehlo()

        # Log in to the server
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Create the email
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = to_address
        message["Subject"] = subject

        # Attach the body with the msg instance
        message.attach(MIMEText(body, 'plain'))

        # Attach a file if provided
        if filename:
            with open(filename, 'rb') as attachment:
                payload = MIMEBase('application', 'octet-stream')
                payload.set_payload(attachment.read())
                encoders.encode_base64(payload)
                payload.add_header('Content-Disposition', f'attachment; filename={os.path.basename(filename)}')
                message.attach(payload)

        # Send the email
        server.sendmail(EMAIL_ADDRESS, to_address, message.as_string())
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        
    finally:
        server.quit()

if __name__ == "__main__":
    # Example usage
    send_email("recipient@example.com", "Test Subject", "This is a test email.", "test_attachment.txt")
