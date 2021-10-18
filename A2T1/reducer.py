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
		cur=nex
		out.append(dest)
	else:
		if nex==cur:
			out.append(dest)
		else:
			#print('node hath changed')
			print(cur,out,sep=',')
			cur=nex
			out=[]
			out.append(dest)
			
print(cur,out,sep=',')
f.close()
