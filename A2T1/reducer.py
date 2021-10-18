#!/usr/bin/env python3
import sys
cur = None
out = []

f = open("v", "a+")

for line in sys.stdin:
	line = line.strip().split('\t')
	nex = int(line[0])   
	dest=int(line[1])
	#print(cur,dest)
	if cur==None:
		# handles the case for the first iteration
		cur=nex
		out.append(dest)
	else:
		if nex==cur:
			# adds out points for each same node
			out.append(dest)
		else:
			# node changed; prints out list and switches to the next node
			print(cur,out,sep=',')

			# writes to file v (inital page ranks)
			f.write(f"{cur},1")
			cur=nex
			out=[]
			out.append(dest)

print(cur,out,sep=',')
f.close()
