import sys

oldstr = sys.argv[2]
newstr = sys.argv[3]

with open(sys.argv[1], 'r') as f:
	for line in f:
		newline = line.replace(oldstr, newstr)
		print(newline, end='')
