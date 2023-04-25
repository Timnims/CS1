import sys
f=open(sys.argv[1],'r')
lines=f.readlines()

cL=[]
c=0
for l in lines:
	
	if str(l) == '\n':
		
		cL.append(c)
		c=0
		continue
	
	c=c+int(l)
	

cl.sort()

print(cl[-1])

f.close()
