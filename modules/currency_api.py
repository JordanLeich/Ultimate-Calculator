"""
Using currencyconverterapi.com API to get some
basic currency-conversion pairings in real-time.
MAX 100 requests/hr.
"""
from requests import get
import json
import os


def validate_key(key):
    url = f'https://free.currconv.com/api/v7/currencies?apiKey={key}'
    data = get(url)
    if data.status_code == 200:
        save_key(key)
        return True
    else:
        return False


def create_key_json():
    with open("key.json", 'w'):
        pass


def save_key(key):
    data = {'key': key}
    with open("../key.json", "w") as outfile:
        json.dump(data, outfile)


def get_currency_pairs():
    """
    List of all possible currency pairings
    available on this API.

    THIS STILL NEEDS WORK TO PUT TOGETHER
    EVERY POSSIBLE CURRENCY COMBINATION.
    """
    api_key = os.environ.get('API_KEY')
    url = 'https://free.currconv.com/api/v7/currencies?apiKey={}'.format(api_key)
    data = get(url)
    currencies = [currency for currency in data.json()['results']]
    pairs = []

    for ind, currency in enumerate(currencies):
        if ind != 0:
            pairs.append('ALL_{}'.format(currency))

    return pairs


def get_currency(req_pair, api_key):
    url = "https://free.currconv.com/api/v7/convert?q={}&compact=ultra&apiKey={}".format(req_pair, api_key)
    data = get(url)
    return data.json()[req_pair]


if __name__ == '__main__':
    urls = "https://api.exchangerate.host/latest?base=USD&symbols=EUR"
    panda = get(urls)
    print(panda.json())
