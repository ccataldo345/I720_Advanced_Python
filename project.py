from datetime import datetime
import requests

# convert a timestamp to python native datetime object
timestamp = 1512864000
d = datetime.fromtimestamp(timestamp)
print(d)


r = requests.get("https://api.blockchain.info/charts/market-price?format=json")
values = r.json()
print(values)