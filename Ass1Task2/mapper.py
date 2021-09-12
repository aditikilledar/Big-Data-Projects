#!/usr/bin/env python3
import sys
import requests
import math
import json
import time

latitude = float(sys.argv[1])
longitude = float(sys.argv[2])
D = float(sys.argv[3])

for l, line in enumerate(sys.stdin):

	data = json.loads(line)
	
	lat = float(data['Start_Lat'])
	lng = float(data['Start_Lng'])
	if lat > -90 and lat < 90:
		if lng > -180 and lng < 80:
			if (lat < latitude + D):
				if (lat > latitude - D):
					if  (lng < longitude + D): 
						if(lng > longitude - D):
							#print(f'im in square lat: {lat}, lng: {lng}')
							#distance = euclidian_distance((lat,lng),(latitude,longitude))
							#start = time.process_time()
							distance = math.sqrt((lat - latitude)**2 + (lng - longitude)**2)
							#end = time.process_time()
							#if end - start > 0.00001:
								#print(f'time for {l}: ',end - start)
								#print(data)
							
							if distance < D:
								body = { "latitude": lat, "longitude": lng }
								#start = time.process_time()
								response = requests.post('http://20.185.44.219:5000/',json=body).json()
								if None not in response.values():
									#print('time: ',time.process_time() - start)
									#print('response: ',response)
									city = response['city']
									state = response['state']
									
									print(f'{state},{city},1')
									#print('response: ',response)
					
					
					
					
					
					
					
					
					
					
