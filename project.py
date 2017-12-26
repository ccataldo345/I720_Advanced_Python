from datetime import datetime
import requests
import json

# from django.http import HttpResponse
# import pandas as pd



# convert a timestamp to python native datetime object
timestamp = 1512604800
d = datetime.fromtimestamp(timestamp)
# print(d)


r = requests.get("https://api.blockchain.info/charts/market-price?format=json")
data = r.json()
'''
date = data['values']['x']
price = data['values']['y']
resDate = HttpResponse(date)
resPrice = HttpResponse(price)
print(resDate, resPrice)
'''

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

#print(list_values)


list = list(zip(list_values, list_dates))

'''
# print all values, dates
for i in range(len(list) ):
	print(list[i][0], ", ", datetime.fromtimestamp(list[i][1]))
'''

# print max value
max_list = max(list)
max_list_value = max_list[0]
max_list_date = max_list[1]
print ()
print ("Max value USD: ", max_list_value, " on date: ", datetime.fromtimestamp(max_list_date))
print ()


# print max increase
max_change_increase_value = 0
max_change_increase_date = None

for i in range(len(list) -1):
	previous = list[i][0]
	current = list[i+1][0]
	change = (current - previous) / previous * 100 
	if change > max_change_increase_value:
		max_change_increase_value = change
		max_change_increase_date = list[i+1][1]
		
print ("Max increase: ", round(max_change_increase_value, 2), "%,  on date: ", datetime.fromtimestamp(max_change_increase_date))
print ()


# print max decrease
max_change_decrease_value = 0
max_change_decrease_date = None

for i in range(len(list) -1):
	previous = list[i][0]
	current = list[i+1][0]
	change = (current - previous) / previous * 100
	if change < max_change_decrease_value:
		max_change_decrease_value = change
		max_change_decrease_date = list[i+1][1]
		
print ("Max decrease: ", round(max_change_decrease_value, 2), "%, on date: ", datetime.fromtimestamp(max_change_decrease_date))
print ()
