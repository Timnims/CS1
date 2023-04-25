n2=0
n1=1
n=0
for i in range(1,21):
    
    n=n1 + n2
    n2 = n1
    n1 = n
    print(f'{i} is: {n}')



