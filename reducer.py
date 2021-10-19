#!/usr/bin/env python3
import sys
import os
cur=None
rank_p=0.15
v1=open(f'{os.getcwd()}/v1','w')

for line in sys.stdin:
	# RANK = 0.15 + 0.85(Sum(contribution(q) for q in outgoing list)) 
	# input - p,q,cont(p,q)
	# output - print p,rank(p) written back to v1
	
	line=line.strip().split(',')
	
	q=int(line[0])
	p=int(line[1])
	cont_pq=float(line[2])
	
	if cur==None:
		cur=q
	if cur==q:
		rank_p += 0.85*cont_pq
	else:
		print(f'{cur},{rank_p:.2f}')
		v1.write(f'{cur},{rank_p:.2f}')
		rank_p=0.15
		cur=q
		
print(f'{cur},{rank_p:.2f}')
v1.write(f'{cur},{rank_p:.2f}')
v1.close()
	
	
	
	
	
