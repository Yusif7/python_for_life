import yagmail
import os
import time
from datetime import datetime
receiver = ['mail@example.com', 'mail2@example.com']
subject = 'This is subject'
contents = """
Here must be the contents of email
"""
while True:
    if datetime.now().hour == 10 and datetime.now().minute == 00:
        my_email = os.getenv('email')
        my_password = os.getenv('password')
        yag = yagmail.SMTP(user=my_email, password=my_password)
        yag.send(to=receiver, subject=subject, contents=contents)
        print('Email sent!')
        # Wait 60 seconds
        time.sleep(60)

