first='Timo'
last='Clement'
age=15

#F-String formatting
print(f'My name is {first} {last}. I am {age}!')

#.Format method
print('My name is {0} {1}. I am age {2}!'.format(first,last,age))
print('My name is {} {}. I am {}!'.format(first,last,age)) #counts up
print('My name is {x} {y}. I am {z}!'.format(x=first,y=last,z=age))

#String concatenation
print('My name is '+first+' '+last+'.'+' I am '+str(age)+'!')


#Comma seperation
print('My name is',first,last,'.','I am',age,'!')

n=1/3
#Field width formatting
print(f'My name is {first:^20} today')
print(f'My name is {first:-^20} today')
print(f'My name is {first:#<20} today')
print(f'My name is {first:*>20} today')
print(f'The ruler is {n:.2f}cm')


#Getting rid of the invisible \n (it will say 123 in 1 line)
print('1', end='')
print('2', end='')
print('3')


#Escape Sequences
print('What\'s your name')


#Two line string in one line
print('This is the first line!\nThis is the second line!')



#Code!!!
