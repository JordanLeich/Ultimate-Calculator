"""
Using currencyconverterapi.com API to get some
basic currency-conversion pairings in real-time.
MAX 100 requests/hr.
"""
import requests


def get_currency_pairs():
    """
    List of all possible currency pairings
    available on this API.

    THIS STILL NEEDS WORK TO PUT TOGETHER
    EVERY POSSIBLE CURRENCY COMBINATION.
    """
    url = 'https://free.currconv.com/api/v7/currencies?apiKey=915c1e08f6ada7ca7704'
    data = requests.get(url)
    currencies = [currency for currency in data.json()['results']]
    pairs = []

    for ind, currency in enumerate(currencies):
        if ind != 0:
            pairs.append(f'ALL_{currency}')

    return pairs


def get_currency(req_pair):
    url = f"https://free.currconv.com/api/v7/convert?q={req_pair}&compact=ultra&apiKey=915c1e08f6ada7ca7704"

    print("Opening API...")
    data = requests.get(url)

    print('Fetching Data...')
    return data.json()[req_pair]


if __name__ == '__main__':
    urls = f"https://api.exchangerate.host/latest?base=USD&symbols=EUR"
    panda = requests.get(urls)
    print(panda.json())
