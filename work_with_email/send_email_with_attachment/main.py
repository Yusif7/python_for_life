import yagmail
import os

receiver = 'hyuga89@mail.ru'

my_mail = os.getenv('email')
my_password = os.getenv('password')

subject = 'Here is a subject'
# Add attachments to your email
contents = ['Here is a contents', 'files/test.txt']

yag = yagmail.SMTP(user=my_mail, password=my_password)
yag.send(to=receiver, subject=subject, contents=contents)
print('Email sent')
