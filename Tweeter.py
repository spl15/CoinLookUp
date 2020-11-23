#!/usr/bin/python
# Author: Stephen Lamalie
# File tweeter.py
from CoinLookV1_0 import getCoinData 
import tweepy


def sendTweet(coinToLook):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("API key", 
        "API secret key")
    auth.set_access_token("Access Token", 
        "Access Token secret")

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    myTweet = getCoinData(coinToLook)
    try:
        api.update_status(myTweet)
        print("Tweet Sent")
    except:
        print("Error during authentication")
