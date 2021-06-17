import requests

url = 'https://api.exchangerate.host/convert?from=USD&to=EUR'
response = requests.get(url)
data = response.json()

for item in data["info"]:
    print(item)
