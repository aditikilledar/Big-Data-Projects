#!/usr/bin/env python3
import sys
import os
cur=None
rank_q=0.15
v1_path=sys.argv[1]
v1=open(v1_path,'w')

for line in sys.stdin:
	# RANK = 0.15 + 0.85(Sum(contribution(q) for q pointing to p)) 
	# input - q,p,cont(p,q)
	# output - print p,rank(p) written back to v1
	
	line=line.strip().split(',')
	
	q=int(line[0])
	p=int(line[1])
	cont_pq=float(line[2])
	
	if cur==None:
		cur=q
	if cur==q:
		rank_q += 0.85*cont_pq
	else:
		print(f'{cur},{rank_q:.2f}')                         
		v1.write(f'{cur},{rank_q:.2f}\n')
		rank_q = 0.15 + (0.85*cont_pq)
		cur=q
		
print(f'{cur},{rank_q:.2f}')
v1.write(f'{cur},{rank_q:.2f}')
v1.close()
	
	
	
	
	
