#!usr/bin/env python3
import sys

res = {i:0 for i in range(24)}

for line in sys.stdin:
    #hour   1
    line=line.split('\t')
    hr = int(line[0])
    res[hr] += 1
    
for key in res.keys():
    if res[key]:
        print(f'{key}\t{res[key]}')