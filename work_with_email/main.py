import yagmail
import os
import time

# Receivers email addresses
receiver = ['mail@example.com', 'mail2@example.com']
subject = 'This is subject'
contents = """
Here must be the contents of email
"""
# Send emails every 60 seconds
while True:
    # Your email address information set by using cmd as administrator with setx command
    my_email = os.getenv('email')
    my_password = os.getenv('password')
    # All emails use the SMTP protocol
    yag = yagmail.SMTP(user=my_email, password=my_password)
    yag.send(to=receiver, subject=subject, contents=contents)
    print('Email sent!')
    # Wait 60 seconds
    time.sleep(60)

