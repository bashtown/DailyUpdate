import smtplib
import email
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

    message = 'Subject: %s\n\n%s' % (sub, msg)

    mail.sendmail(email_id, to, message)
    print 'Message sent.'


