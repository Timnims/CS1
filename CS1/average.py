tot=0
avg=0
while True:
    num=input('Enter Number: ')
    if num=='quit':
        break
        
    else:
        tot=int(tot)
        avg=int(avg)
        avg=avg+1
        tot=tot+int(num)
        print(f'Total: {tot}')

print(f'Average was: {tot/avg}')   

#Adds numbers user inputs until they input 0 and shows average number
