import smtplib
import email
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import oauth2
import base64
import json

def sendUpdate(msg, to, sub="Daily Update"): #Can specify a custom subject line or use default.
    with open('credential.json') as j:
        cred = json.load(j)
    
    email_id=cred['installed']['email_id']
    client_id=cred['installed']['client_id']
    client_secret=cred['installed']['client_secret']
    refresh_token=cred['installed']['refresh_token']
    response = oauth2.RefreshToken(client_id,client_secret,refresh_token)

    access_token=response['access_token']
    oauth2String = oauth2.GenerateOAuth2String(email_id,access_token,base64_encode=True)
    mail = smtplib.SMTP('smtp.gmail.com:587')
    mail.ehlo()
    mail.starttls()
    mail.ehlo()

    mail.docmd('AUTH','XOAUTH2 ' + oauth2String)

    message = MIMEMultipart('alternative')
    message['Subject'] = sub
    html = MIMEText(msg.encode('utf-8'), 'html', 'utf-8')
    message.attach(html)
    mail.sendmail(email_id, to, message.as_string())
    print 'Message sent.'
