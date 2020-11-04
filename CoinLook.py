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
        return  'Down -' + str(num) + '%' 
    else:
        num = num * 1.00
        return 'Up +' + str(num) + '%'

def extractData(jsonObj):
    print('Name: ' + str(jsonObj['name']), end=' ')
    print('Symbol: ' + str(jsonObj['symbol']),end='  ')
    for attribute,value in jsonObj.items():
        if str(attribute) == 'quote':
            for att,val in value.items():
                for at,va in val.items():
                    if at == 'price':
                        print(str('{:.5f}'.format(va)))
                    if at == 'percent_change_24h':
                        num = round(va,4)
                        print('Percent Change in a Day: ' + upOrDown(num), end='  ')
                    if at == 'percent_change_7d':
                        num = round(va,4)
                        print('Percent Change in a Week: ' + upOrDown(num), end='\n\n')

cmc = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(cmc.content, 'html.parser')
 
data = soup.find('script',id="__NEXT_DATA__",type="application/json") 

coins = {}
# remove script tags
coin_data = json.loads(data.contents[0])
listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
for i in listings:
    myString = str(i['name'])
    if myString == 'Bitcoin' or myString == 'Litecoin' or myString == 'Monero' or myString == 'Ethereum':
        extractData(i)
