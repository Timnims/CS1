import random
L=[]
while len(L) <40:
	n=random.randrange(10,100)
	if n not in L:
		L.append(n)
L.sort()
print(L)

