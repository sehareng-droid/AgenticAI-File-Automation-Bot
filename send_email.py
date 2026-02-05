import os
import smtplib
from email.message import EmailMessage

#2 step verification through application password(16 charcter password with google security)
def send_email(to_email, subject, body):
     email_address = os.getenv('Email_address')
     email_password=os.getenv('Email_password')

     

     msg=EmailMessage()
     msg['From'] = email_address
     msg['To'] = to_email
     msg['subject'] = subject
     msg.set_content(body)

     print (email_address)
     print(email_password)

     with smtplib.SMTP("smtp.gmail.com",587) as server:
          server.starttls()
          server.login(email_address,email_password)
          server.send_message(msg)
