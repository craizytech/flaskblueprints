"""

mail -> simple mail transfer protocol (SMTP)
security options:
    - ssl (secure shell layer)
    - tls (transport layer security)
    
    - ssl: port 465
    - tls: port 587
    
python packages
    - smtplib
    - mail
    - ssl
    
    tls - updated version of ssl
    

    """
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# func to send email
def send_email(email_address):
    port = 465  # using SMTP_SSL()
    password = "sqmzguzsqzpxibuy"

    sender_gmail = "muchemi7857@gmail.com"
    recepient_gmail = email_address
    subject = "Test Message from Muchemi"
    body = """
    Hujambo! Ruto Must Go.
    """


    msg = MIMEMultipart()
    msg["From"] = sender_gmail
    msg["To"] = email_address
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))


    # Create secure ssl context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port=port, context=context) as server:
        server.login(sender_gmail, password)
        server.sendmail(sender_gmail, recepient_gmail, msg.as_string())
        print("Email sent successfully")
