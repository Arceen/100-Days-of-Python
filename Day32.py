# # Day 32 Email SMTP and Manage Dates (Datetime)
import smtplib
import random
import datetime as dt
from email.message import EmailMessage
import pandas

# my_email = "faketester6000@yahoo.com"
# password = "vtqnlafqmpqtfgdw"
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
# connection.starttls()
# message = 'Subject: Sending an invitation\nTo be fair you should be the one sending me Niloy'
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="faketester6000@gmail.com", msg=message)
# connection.close()
# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()    
# print(day_of_week)

# date_of_birth = dt.datetime(year=1996, month=12, day=28)
# print(date_of_birth)

# current_day = dt.datetime.now().weekday()

# if current_day == 5:
#     quotes = []
#     with open('Day32_quotes.txt') as f:
#         quotes = f.readlines()
#     message = random.choice(quotes)
#     print(message)
    
#     my_email = "faketester6000@yahoo.com"
#     password = "vtqnlafqmpqtfgdw"
#     connection = smtplib.SMTP_SSL('smtp.mail.yahoo.com')
    
#     msg = EmailMessage()
#     msg.set_content(message)
#     msg['Subject'] = 'Weekly Quotes'
#     msg['From'] = my_email
#     msg['To'] = "faketester6000@gmail.com"

#     # Send the message via our own SMTP server.
    
#     connection.login(user=my_email, password=password)
#     connection.send_message(msg)
#     connection.close()

# birthday wisher automated
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

data = pandas.read_csv('Day32_birthdays.csv').to_dict(orient='records')
today = dt.datetime.now()
day = today.day
month = today.month
bday_list = []
for row in data:
    if row['day'] == day and row['month'] == month:
        bday_list.append(row)

if len(bday_list)>0:
    my_email = "faketester6000@yahoo.com"
    password = "vtqnlafqmpqtfgdw"
    connection = smtplib.SMTP_SSL('smtp.mail.yahoo.com')
    connection.login(user=my_email, password=password)
    for i in bday_list:
        print(f"Sending message to: {i['name']}")
        file_name = random.randint(1, 3)
        message = ' Happy Birthday '
        with open('Day32_letter_templates/letter_'+str(file_name)+'.txt') as f:
            message = f.read()
            message = message.replace('[NAME]', i['name'])
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = '🎉Happy Birthday🎉'
        msg['From'] = my_email
        msg['To'] = i['email']
        connection.send_message(msg)

    connection.close()

