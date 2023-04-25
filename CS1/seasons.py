running=True
while running:
	month=input('Type the first three letters of a month or END to end: ')

	if month.upper()=='JAN' or month.upper()=='FEB' or month.upper()=='DEC':
		print('That month is in winter!\n')
	elif month.upper()=='MAR' or month.upper()=='APR' or month.upper()=='MAY':
		print('That month is in spring!\n')
	elif month.upper()=='SEP' or month.upper()=='OCT' or month.upper()=='NOV':
		print('That month is in fall!\n')
	elif month.upper()=='JUN' or month.upper()=='JUL' or month.upper()=='AUG':
		print('That month is in summer!\n')
	elif month.upper()=='END':
		print('Ending')
		running = False
	else:
		print('Invalid month, make sure that you enter the first three letters of the month!')
	#Tells you which season the month is in
