##########3emails.py###################

#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject,body, attachment):
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    attachment_file = os.path.basename(attachment)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/',1)
    with open(attachment, 'rb') as ap:
        message.add_attachment(ap.read(),maintype=mime_type, subtyp$
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()