"""
Using currencyconverterapi.com API to get some
basic currency-conversion pairings in real-time.
MAX 100 requests/hr.
"""

from urllib.request import urlopen
import json


def get_api_key():
    with open('keys.json', 'r') as keys:
        data = json.load(keys)
        api_key = data['api_key']
    return api_key


def get_currency_pairs():
    """
    List of all possible currency pairings
    available on this API.

    THIS STILL NEEDS WORK TO PUT TOGETHER
    EVERY POSSIBLE CURRENCY COMBINATION.
    """
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
            i += 1
    return pairs


def get_currency(req_pair):
    url = (
        'https://free.currconv.com/api/v7/convert'
        f'?q={req_pair}'
        '&compact=ultra'
        f'&apiKey={get_api_key()}'
    )

    with urlopen(url) as response:
        source = response.read()
    data = json.loads(source)
    return data[req_pair]
