#!/usr/bin/python
# Author: Stephen Lamalie
# File Mail.py
from Tweeter import sendTweet 
from datetime import datetime
import time

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    tweet_time = "22:15:00"
    if current_time == tweet_time:
        sendTweet('Bitcoin')
        sendTweet('Ethereum')
        sendTweet('Litecoin')
        sendTweet('Stellar')
        time.sleep(60)