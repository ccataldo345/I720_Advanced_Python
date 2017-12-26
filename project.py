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

# print max value
max_list = max(list)
print ()
print ("Max value USD: ", max_list[0], " on date: ", datetime.fromtimestamp(max_list[1]))
print ()

# print greatest percent increase over the previous day
print ("day 0: ", list[0][0])
print ("day 1: ", list[1][0])
print ("diff: ", list[1][0] - list[0][0])
max_diff = round((list[1][0] - list[0][0])/list[0][0], 5)
print("diff %: ", max_diff, "%")
print ()


min = list[0][0]
max = list[0][0]
max_diff = -1


count=0
max = 0
'''
for value, date in list:
	count = count + 1
	diff = value[1] - value
	
	
	# if (max_i > max):
		# max = max_i
		
	print(diff)
'''	


print (type(list))
print (len(list))
value = list[364][0]
date = list[364][1]
print (value, " on date: ", datetime.fromtimestamp(date))
