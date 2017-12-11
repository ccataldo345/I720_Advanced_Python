from datetime import datetime
import requests
import json
import numpy

# convert a timestamp to python native datetime object
timestamp = 1512604800
d = datetime.fromtimestamp(timestamp)
# print(d)


r = requests.get("https://api.blockchain.info/charts/market-price?format=json")
data = r.json()

#print(data['values'])

list_dates = []
list_values =[]

#print dates:
for num in data['values']:
	#date = datetime.fromtimestamp(num['x'])
	date = num['x']
	value = num['y']
	list_dates.append(date)
	list_values.append(value) 

#print(date, "; ", value)
#print(list_dates)

list = list(zip(list_values, list_dates))

# print max value
max_list = max(list)
print ("Max value USD: ", max_list[0], " on date: ", datetime.fromtimestamp(max_list[1]))
