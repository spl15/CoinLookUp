#!/usr/bin/python
# Author: Stephen Lamalie
# File Mail.py
from MyMail import mail_me
from datetime import datetime
import time

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    email_time = "23:59:00"

    if current_time == email_time:
        mail_me()
        time.sleep(60)