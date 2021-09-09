import datetime
import sys
import json

# print('it runs')

l = 0

for line in sys.stdin:
    
    #  --------------------
    l+=1
    # print(l, "is line #")
    #  ---------------
    curr_data = json.loads(line)
    dsc = ['lane blocked','shoulder blocked','overturned vehicle']
    wc = ["heavy snow","thunderstorm","heavy rain","heavy rain showers","blowing dust"]
    condition_count = 0
    # check for lowercase and uppercase of each string
    if any(ele in curr_data['Description'].lower() for ele in dsc):
        condition_count += 1
        # print("Description passed in line", l)
        
        if curr_data['Severity'] >= 2:
            condition_count += 1
            # print("Severity passed in line", l)
    
            if curr_data['Sunrise_Sunset'] == 'Night':
                condition_count += 1
                # print("Sunrise_Sunset passed in line", l)
    
                if curr_data['Visibility(mi)'] <= 10:
                    condition_count += 1
                    # print("Visibility passed in line", l)
    
                    if curr_data['Precipitation(in)'] >= 0.2:
                        condition_count += 1
                        # print("Precipitation passed in line", l)
    
                        if any(ele == curr_data['Weather_Condition'].lower() for ele in wc):
                            condition_count += 1
                            # print("Weather_Condition passed in line", l)

                            # if condition_count == 6:
                            # print("LESGO")
                            #2016-10-04 08:03:58
                            # if an accident spans more than an hour in end_time - start_time,
                            # do we print two outputs ??
                            hour = int(curr_data['Start_Time'][11:13])
                            print(f'{hour}\t1')

                            # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
