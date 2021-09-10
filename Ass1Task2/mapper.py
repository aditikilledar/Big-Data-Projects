#!/usr/bin/env python3
import sys
import requests
import math
import json
import datetime

def euclidian_distance(co_ord, given_point):
	
	lat1 = co_ord[0]
	lng1 = co_ord[1]
	
	lat2 = given_point[0]
	lng2 = given_point[1]
	
	distance = math.sqrt((lat1 - lat2)**2 + (lng1 - lng2)**2)
	#print('distance: ',distance)
	return distance

latitude = float(sys.argv[1])
longitude = float(sys.argv[2])
D = float(sys.argv[3])

for line in sys.stdin:
	data = json.loads(line)
	
	lat = float(data['Start_Lat'])
	lng = float(data['Start_Lng'])
	
	distance = euclidian_distance((lat,lng),(latitude,longitude))
	if distance < D:
		body = { "latitude": lat, "longitude": lng }
		response = requests.post('http://20.185.44.219:5000/',json=body).json()
		#print('response: ',response)
		city = response['city']
		state = response['state']
		
		print(f'{state}\t{city}\t1')
		#print('response: ',response)
