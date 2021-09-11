#!/usr/bin/env python3
import sys

#first = sys.stdin.read().split(',')
curr_state = None 
curr_city = None
state_count = 1
city_count = 1

for line in sys.stdin:
	
	line = line.split(',') #THANK GOD
	#print(line)
	if line[0] != '\t\n':
		#print('not a khali line')
		state = line[0]
		city = line[1]
		
		#print(state, city)
		if curr_state == state: #if the state in the line is the same as curr_state
			#print('still same state')
			state_count += 1
			if curr_city == city: # if curr_city matches the city in the 'line'
				#print('same city')
				city_count += 1
				
			else: # if city changes
				#print('city changed')
				print(f'{curr_city} {city_count}')
				
				city_count = 1
				curr_city = city
				
		else: # if state changes
			#print('state changed')
			#change curr_city
			if curr_state:
				print(f'{curr_city} {city_count}')
				print(f'{curr_state} {state_count}')
				print(state)
				
			else:
				print(state)
			state_count = 1	
			city_count = 1
			curr_city = city
			curr_state = state
			
if curr_state == state:
	if curr_city == city:
		print(f'{curr_city} {city_count}')
	else:
		print(f'{city} 1')
	print(f'{curr_state} {state_count}')
else:
	print(state)
	print(f'{city} {1}')
	print(f'{state} 1')
