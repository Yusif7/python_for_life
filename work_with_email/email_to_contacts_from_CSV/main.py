import pandas
import yagmail
import os

receiver = ['mail@example.com', 'mail2@example.com']
subject = 'This is subject'

my_email = os.getenv('email')
my_password = os.getenv('password')
yag = yagmail.SMTP(user=my_email, password=my_password)

# Construction for showing us content of csv file
df = pandas.read_csv('contacts.csv')

# Iterate over all contacts in csv file
for col, row in df.iterrows():
    # Filepath of txt files in third column of csv file
    contents = [f"""
    Hi {row['name']}
    Here must be the contents of email
    """, {row['filepath']}]
    # Send to email row
    yag.send(to=row['email'], subject=subject, contents=contents)
    print('Email sent!')




