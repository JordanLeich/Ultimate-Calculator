import requests

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
data = response.json()

print(data)
