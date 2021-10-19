
#!/usr/bin/env python3
import sys
import os
cur = None
v_path=sys.argv[1]
f = open(v_path,'w')

for line in sys.stdin:
	line = line.strip().split('\t')
	#print(line)
	nex = int(line[0])   
	dest=int(line[1])
	#print(cur,dest)
	if cur==None:
		# handles the case for the first iteration
		cur=nex
		print(f'{cur}\t[{dest}',end='')
		#out.append(dest)
	else:
		if nex==cur:
			# adds out points for each same node
			#out.append(dest)
			print(f',{dest}',end='')
		else:
			# node changed; prints out list and switches to the next node
			#print(cur,out,sep=',')

			# writes to file v (inital page ranks)
			#print('writing into file now')
			f.write(f"{cur},1\n")
			cur=nex
			print(']')
			print(f'{cur}\t[{dest}',end='')
			#out=[]
			#out.append(dest)

print(']')
#f.write('in file')
#print('writing into file now')
f.write(f"{cur},1\n")
f.close()
