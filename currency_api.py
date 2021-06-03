'''
Using freeforexapi.com API to get some basic 
currency-conversion pairings in real-time. 
MAX 100 requests/hr. 
'''

from urllib.request import urlopen
import json

def get_api_key():
    with open('keys.json','r') as keys:
            data = json.load(keys)
            api_key = data['api_key']
    return api_key

def get_currency_pairs():
    '''
    List of all possible currency pairings
    available on this API.

    THIS STILL NEEDS WORK TO PUT TOGETHER
    EVERY POSSIBLE CURRENCY COMBINATION.
    '''
    api_key = get_api_key()
    url = f'https://free.currconv.com/api/v7/currencies?apiKey={api_key}'
    with urlopen(url) as response:
        source = response.read()
        data = json.loads(source)
    currencies = []
    for currency in data['results']:
        currencies.append(currency)
    pairs = []
    i = 1
    for currency in currencies:
        while i < len(currencies):
            pairs.append(f'{currency}_{currencies[i]}')
            i+=1
    return pairs


# TEMP LIST OF PAIRS
pairs = [
        "EUR_USD",
        "EUR_GBP",
        "GBP_USD",
        "USD_JPY",
        "AUD_USD",
        "USD_CHF",
        "NZD_USD",
        "USD_CAD",
        "USD_ZAR"
        ]


def get_currency(req_pair):
    api_key = get_api_key()
    url = (
            'https://free.currconv.com/api/v7/convert'
            f'?q={req_pair}'
            '&compact=ultra'
            f'&apiKey={api_key}'
          )

    with urlopen(url) as response:
        source = response.read()
    data = json.loads(source)
    print(data) # CAN BE REMOVED, USEFUL FOR DEBUGGING
    return data


def tests():
    get_currency(pairs[0])
    get_currency(pairs[1])
    get_currency(pairs[2])
    get_currency(pairs[3])
    get_currency(pairs[4])
    get_currency(pairs[5])
    get_currency(pairs[6])
    get_currency(pairs[7])
    get_currency(pairs[8])
