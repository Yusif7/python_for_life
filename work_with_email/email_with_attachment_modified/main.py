import pandas
import yagmail
import os

# Sender information
my_email = os.getenv('email')
my_password = os.getenv('password')
yag = yagmail.SMTP(user=my_email, password=my_password)

# Construction for showing us content of csv file
df = pandas.read_csv('contacts.csv')


# Function for creating new file for sending
def generate_file(filename, content):
    with open(filename, 'w') as file:
        # We need to change the format of filename because the content inside of file must be a string
        file.write(str(content))


# Iterate over all contacts in csv file
for col, row in df.iterrows():
    # Create variables for clean code
    name = row['name']
    amount = row['amount']
    # Add suffix .txt to file name
    # The name of attached file
    filename = name + '.txt'

    # Call the function inside of loop for create file for each contacts if there are more than one
    generate_file(filename, amount)

    subject = 'This is subject'
    # Filepath of txt files in third column of csv file
    contents = [f"""
    Hi {name}
    You have to pay {amount}
    Attached file is in email.
    """, filename]
    # Send to email row
    yag.send(to=row['email'], subject=subject, contents=contents)
    print('Email sent!')
