#!/usr/bin/env python3
import sys
import os

v_path=sys.argv[1]
emb_path=sys.argv[2]
v=open(v_path, 'r')

for line in sys.stdin:
	#op - p,q,contr(p,q)
	# format - p [list of outgoing ids (comma sep)]
	# define contribution function
	# contribution = existing_rank(p) x similarity(node, dest) / len of list (except 0)
	# similarity = embedding(p).embedding(q) / magnitude(p).magnitude(q)
	# RANK = 0.15 + 0.85(Sum(contribution(q) for q in outgoing list)) 
	
	q_order = [] #to store value of outgoing nodes as they are found in the embedding file.
	
	line=line.split('\t')
	p=int(line[0]) # source node
	q=[] # destination nodes
	
	outgoing=line[1].strip()
	outgoing = outgoing[1:-1].split(',')
	
	for out in outgoing:
		q.append(int(out))
	
	# finding rank of p from v file
	v_line=v.readline()
	v_line=v_line.split(',')
	
	if p == float(v_line[0]):
		p_rank = float(v_line[1])
		#print(p, v_line[1])
	else:
		print('oops')
	
	count = 1
	reached = False # for reaching p
	reached_q = False # for reaching q
	vec_count=0 # to store next 5 from embedding
	p_vector=[] # stores embedding vector for p
	q_vector=[] # stores embedding vector(s) for all q corresponding to p
	
	emb=open(emb_path,'r')
	for i,emb_line in enumerate(emb): # to read line by line
		#print(i,count)
		if i==count:
			emb_line=emb_line.split('"')
			#print(p, emb_line[1])
			if len(emb_line) > 1:
				if float(emb_line[1]) == p:
					#print('reached p')
					reached=True
				if float(emb_line[1]) in q:
					#print('reached q')
					reached_q=True
					q_order.append(int(emb_line[1]))
			count+=7
		elif reached:
			#print(float(str(emb_line).strip().split(',')[0]))
			p_vector.append(float(str(emb_line).strip().split(',')[0]))
			#print(p_vector)
			vec_count+=1
			if vec_count == 5:
				reached = False
				vec_count=0
			
		elif reached_q:
			#print(float(str(emb_line).strip().split(',')[0]))
			q_vector.append(float(str(emb_line).strip().split(',')[0]))
			vec_count+=1
			if vec_count == 5:
				reached_q = False
				vec_count=0
				
	print(p, p_vector, q_order, q_vector)
		
	#TODO
	# calculate similarity -> calculate contribution from updated v (1/len(outgoing)) 
	# print output - p,q,contribution(p,q)

