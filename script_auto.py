import time, datetime
import hashlib
from urllib.request import urlopen, Request
import smtplib
import ssl
from email.message import EmailMessage

url = Request('https://news.ycombinator.com/', headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(url).read()

currentHash = hashlib.sha224(response)
print(currentHash)
print(currentHash)
print(response)
time.sleep(5)
print('5 seconds passed')
while True:
    try:
        time.sleep(30)
        response = urlopen(url).read()
        new_hash = hashlib.sha224(response).hexdigest()
        if new_hash == currentHash:
            continue
        else:
            print('something changed')
            port = 465
            smtp_server = 'smtp.gmail.com'
            reciever_email = 'jftennis@gmail.com'
            sender_email = 'jamesfdata@gmail.com'
            password = 'two'
            subject = 'Website notification change'
            message = '''
            changes have applied to your website please check them out and see what has happened!
            '''
    except Exception as e:
        print(e)
