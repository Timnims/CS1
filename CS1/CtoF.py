running=True
print('Enter CtoF to convert celcius to fahrenheit or FtoC to convernt fahrenheit to Celcius or END to end the program')
while running:
	temp=input('CtoF or FtoC: ')

	if temp.lower()=='ctof':
		far1=int(input('Enter temperature in Celcius: '))
		cel1=(far1 * 9/5) + 32
		print(f'Temperature in Fahrenheit is: {cel1}\n')
	elif temp.lower()=='ftoc':
		cel=int(input('Enter temperature in Fahreheit: '))
		far = 5/9 * (cel-32)
		print(f'Temperature in Celcius is: {far}\n')
	elif temp.lower()=='end':
		print('Ending')
		running = False
	else:
		print('Error, That is not a valid input')
#Simple Temperature Converter
