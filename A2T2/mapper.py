#!/usr/bin/env python3
import sys
import json
import os

v_path=sys.argv[1]
emb_path=sys.argv[2]

v=open(v_path,'r')
emb=open(emb_path,'r')

embedding=json.loads(emb.read())

for line in sys.stdin:
	# format - p [list of outgoing ids (comma sep)]
	# define contribution function
	# contribution = existing_rank(p) x similarity(node, dest) / len of list (except 0)
	# similarity = embedding(p).embedding(q) / magnitude(p).magnitude(q)
	# RANK = 0.15 + 0.85(Sum(contribution(q) for q in outgoing list)) 
	contribution=0
	line=line.split('\t')
	p=int(line[0])
	p_vec = embedding[str(p)]
	outgoing=line[1].strip()
	outgoing = outgoing[1:-1].split(',')
	
	v_line=v.readline()
	v_line=v_line.split(',')
	
	if p == float(v_line[0]):
		p_rank = float(v_line[1])
		if len(outgoing) > 0:
			p_rank = p_rank/len(outgoing)
		#print(p, v_line[1])
	else:
		print('oops')
	#rank is available from here
	
	for q in outgoing:
		q_vec = embedding[str(q)]
		dot=0
		mag_p=0
		mag_q=0
		similarity=0
		for j in range(len(p_vec)):
			mag_p += p_vec[j]*p_vec[j]
		mag_p = mag_p**(0.5)
		for k in range(len(q_vec)):
			mag_q += q_vec[k]*q_vec[k]
		mag_q = mag_q**(0.5)
		#for i in range(5):
		#	dot += float(q_vec[i])*float(p_vec[i])
		#if mag_p == 0 or mag_q == 0:
		#	similarity=0
		#else:
		#	similarity = dot/(mag_p*mag_q)
		#cont = p_rank*similarity
		#print(f'{q},{p},{cont}')
		print(mag_p,mag_q,1)
		
		
		
		
