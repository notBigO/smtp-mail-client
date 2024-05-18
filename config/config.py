import os

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'your_email@gmail.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_password')
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
