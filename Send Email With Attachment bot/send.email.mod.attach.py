# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 22/02/2023
# REVISED DATE: 22/02/2023
# PURPOSE: Create a Python Script that sends email with modified attachment to contacts by iterating over a list of emails

# import module
# import the yagmail library
import yagmail
# import the os library
import os
# import the pandas library
import pandas

# declare the variable sender email
sender = 'Input your email here'

# defines the user as sender, password gotten from environment variables
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD(the variable name for the password stored locally'))

# use pandas to create a dataframe by reading the csv file
df = pandas.read_csv('provide path to your contacts.csv here')

# function for generating file, takes in two variables filename and content
def generate_file(filename, content):
    # open the filename to write
    with open(filename, 'w') as file:
        # writes content to file
        file.write(str(content))

# loop to iterate over the rows in the csv file
for index, row in df.iterrows():
    # assigns row[name] to name
    name = row['name']
    # assigns filename to name + .txt
    filename = name + ".txt"
    # assigns row[amount] to amount
    amount = row['amount']
    # assigns row[email] to receiver_email
    receiver_email = row['email']

    # use the function generate_file
    generate_file(filename, amount)

    # contents of email message
    subject = "The subject starts here!"
    contents = [f"""
    Howdy, {name} you are due to pay {amount}
    Utility Bill is attached!""",
    filename,]

    # function to send the email with subject, and contents
    yag.send(to=receiver_email, subject=subject, contents=contents)
    print("Email Sent!")
