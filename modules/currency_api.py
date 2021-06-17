"""
Using currencyconverterapi.com API to get some
basic currency-conversion pairings in real-time.
MAX 100 requests/hr.
"""
from requests import get
import os


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
