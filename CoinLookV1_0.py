#!/usr/bin/python
# Author: Stephen Lamalie
# File CoinLook.py
from bs4 import BeautifulSoup
import requests
import json
import time
def upOrDown(num):
    if num < 0:
        num = num * (-1.00)
        return  ' -' + str(num) + '%' 
    else:
        num = num * 1.00
        return ' +' + str(num) + '%'

def extractData(jsonObj):
    coinString = ''
    coinString = coinString + str(jsonObj['name']) + ' '
    coinString = coinString + 'Symbol: ' + str(jsonObj['symbol']) + '  '
    coinString = coinString + '$'
    for attribute,value in jsonObj.items():
        if str(attribute) == 'quote':
            for att,val in value.items():
                for at,va in val.items():
                    if at == 'price':
                       coinString = coinString + str('{:.5f}'.format(va)) + ' USD '
                    if at == 'percent_change_24h':
                        num = round(va,4)
                        coinString = coinString + 'Percent Change in a Day: ' + upOrDown(num) + '  '
                    if at == 'percent_change_7d':
                        num = round(va,4)
                        coinString = coinString + 'Percent Change in a Week: ' + upOrDown(num) + '\n\n'
    return coinString

def getCoinData(coinToCheck):
    coinString = 'Check Out Today\'s price for '
    cmc = requests.get('https://coinmarketcap.com/')
    soup = BeautifulSoup(cmc.content, 'html.parser')
 
    data = soup.find('script',id="__NEXT_DATA__",type="application/json") 

    coins = {}
    # remove script tags
    coin_data = json.loads(data.contents[0])
    listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
    for i in listings:
        myString = str(i['name'])
        if myString == coinToCheck:
            coinString = coinString + extractData(i)

    coinString = coinString + 'Visit my Owners Website at\n www.stephenlamalie.tk\n...beep boop bop\n\n-py botty'
    return coinString

