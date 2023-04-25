import sys

substr=sys.argv[1]
filename=sys.argv[2]

with open(filename,'r') as f:
	for line in f:
		if substr in line:
			print(line, end='')
