##################### Hard Starting Project ######################
import datetime
from dotenv import load_dotenv
import os
import random
import smtplib
import pandas as pd

load_dotenv()
my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

today = datetime.datetime.now()
todays_date = (today.month, today.day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if todays_date in birthdays_dict:
    letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    bday_person = birthdays_dict[todays_date]

    with open(letter) as bday_letter:
        birthday_wish = bday_letter.read()
        birthday_wish = birthday_wish.replace("[NAME]", bday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=bday_person['email'], msg=f"Subject:Happy Birthday {bday_person['name']}!!\n\n{birthday_wish}")





