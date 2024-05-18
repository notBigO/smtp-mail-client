# Email Sender

A simple Python project to send emails with attachments using SMTP.

## Project Description

This project is designed to send emails with or without attachments using Python's `smtplib` and `email` libraries. It securely handles email credentials and configurations using environment variables.

## Features

- Send plain text emails
- Attach files to emails
- Securely handle email credentials
- Clear and well-structured project organization
- Comprehensive error handling

## Setup

### Prerequisites

- Python 3.x installed
- A Gmail account (or other SMTP-compatible email service)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/email_sender.git
   cd email_sender
   ```

2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate
    `venv\Scripts\activate`
    ```
3. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Configure your email credentials. Create a .env file in the root directory and add your email credentials
    ```env
    EMAIL_ADDRESS=your_email@gmail.com
    EMAIL_PASSWORD=your_password
    ```