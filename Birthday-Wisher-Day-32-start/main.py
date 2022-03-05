import datetime
from dotenv import load_dotenv
import os
import random
import smtplib

load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

now = datetime.datetime.now()
day = now.weekday()
if day == 5 :
    with open('quotes.txt') as quotes:
        quote_lines = quotes.readlines()
        quote = random.choice(quote_lines)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # connection.connect("smtp.gmail.com", 587)
        # connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.getenv("TARGET_EMAIL"),
            msg=f"Subject:Quote of the day!!\n\n{quote}")

