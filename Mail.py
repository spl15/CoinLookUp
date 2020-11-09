#!/usr/bin/python
# Author: Stephen Lamalie
# File Mail.py
from datetime import datetime
from CoinLookV1_0 import getCoinData 
import smtplib

# its me! pyyy botty
gmail_user = 'pybottyy@gmail.com'
gmail_password = 'ADRstreet#'

# get the coin data and put into a string to pass off into email
coinData = getCoinData()

sent_from = gmail_user
to = ['spl15@students.uwf.edu']
subject = 'check out these new coin prices!'


body = """\
check out the latest coin prices. 
Feel free to contact me to add to
the list of coins or stats; or to 
be removed from this mailing list'

%s

Visit my Owners Website at   %s
...beep boop bop
-py botty'
""" % (coinData , "www.stephenlamalie.tk")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    email_time = "22:00:00"

    if current_time == email_time:
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            print('Email Sent Successfully')

        except:
            print('Something went wrong...')

