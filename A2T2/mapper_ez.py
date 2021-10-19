#!/usr/bin/env python3
import sys
import json
import os
import math

#v_path=sys.argv[1]
#emb_path=sys.argv[2]

v=open(f'{os.getcwd()/v}','r')
emb=open(f'{os.getcwd()/embedding_1percent.json}','r')
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
		mag_p=math.sqrt(sum(j**2 for j in p_vec))
		mag_q=math.sqrt(sum(k**2 for k in q_vec))
		for i in range(5):
			dot+=q_vec[i]*p_vec[i]
		similarity = dot/(mag_p*mag_q)
		cont = p_rank*similarity
		print(f'{q},{p},{cont}')
		
		
	
	#print(embedding[str(p)])
	
