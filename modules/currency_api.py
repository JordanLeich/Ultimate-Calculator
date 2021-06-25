"""
Using currencyconverterapi.com API to get some
basic currency-conversion pairings in real-time.
MAX 100 requests/hr.
"""
import requests
import json
import os


def get_api_key():
    """
    Returns a valid api key
    Loads from key.json if possible
    Prompting the user otherwise
    """
    if os.path.exists('key.json'):
        try:
            with open('key.json', 'r') as key_file:
                key = json.load(key_file)
            key = key['key']
        except (IndexError, json.decoder.JSONDecodeError):
            print('key.json is corrupted')
            key = _create_new_api_key()
            _save_key(key)
        if not _validate_key(key):
            print('Invalid key found')
            key = _create_new_api_key()
            _save_key(key)
    else:
        key = _create_new_api_key()
        _save_key(key)
    return key


def _create_new_api_key():
    print("""To use the currency conversion an API key is required.
Visit www.currencyconverterapi.com and follow the steps to get an API key.""")
    while True:
        key = input("API Key: ")
        if _validate_key(key):
            break
        else:
            print('Not a valid key')
    print()
    return key


def _validate_key(key):
    url = f'https://free.currconv.com/api/v7/currencies?apiKey={key}'
    data = requests.get(url)
    if data.status_code == 200:
        return True
    return False


def _save_key(key):
    data = {'key': key}
    with open("key.json", "w") as outfile:
        json.dump(data, outfile)
        outfile.flush()


def get_currencies(api_key):
    """
    List of all currencies available on this API.
    """
    url = 'https://free.currconv.com/api/v7/currencies?apiKey={}'.format(api_key)
    data = requests.get(url)
    return list(data.json()['results'].values())


def get_currency(currency_1, currency_2, api_key):
    """
    Gets the exchange rate between two currencies
    """
    currency_pair = currency_1 + '_' + currency_2
    url = "https://free.currconv.com/api/v7/convert?q={}&compact=ultra&apiKey={}".format(currency_pair, api_key)
    data = requests.get(url)
    return data.json()[currency_pair]

