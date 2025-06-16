import os 
from dotenv import load_dotenv
import csv
import smtplib
from email.message import EmailMessage
import mimetypes

load_dotenv()

COMMIT_FILE = os.getenv("COMMIT_FILE")
SENDER = os.getenv("FROM") 
PASSWORD = os.getenv("PASSWORD")

message = EmailMessage()
with open(COMMIT_FILE, 'rb') as file:
    content = file.read()
    message.set_content("Hello, you can find below the list of weekly commits done by the team" + content.decode('utf-8'))
    maintype, subtype = mimetypes.guess_type(COMMIT_FILE)[0].split('/')
    message.add_attachment(content, maintype=maintype, subtype=subtype, filename=COMMIT_FILE)

message['Subject'] = 'Weekly Commit Report'  
message['From'] = os.getenv("FROM")  
message['To'] = os.getenv("TO")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()        # Starts secure connection
server.login(SENDER, PASSWORD)  # Login to the email server
print("Login successful!")
server.send_message(message)
print("Email sent successfully!")
server.quit()  # Close the connection