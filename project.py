from datetime import datetime
import requests
import json

# convert a timestamp to python native datetime object
timestamp = 1512864000
d = datetime.fromtimestamp(timestamp)
print(d)

r = requests.get("https://api.blockchain.info/charts/market-price?format=json")
data = r.json()

#print(data['values'])

#print dates:
for num in data['values']:
	date = datetime.fromtimestamp(num['x'])
	value = num['y']
	print(date, "; ", value)

