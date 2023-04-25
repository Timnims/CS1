'''
for i in range(1,11):
    print(i)
else:
    print('Done\n')
#1-10
for i in range(10,0,-1):
    print(i)
else:
    print('Done\n')
#10-1
for i in range(10,101,10):
    print(i)
else:
    print('Done\n')
#10 - 100 (going up by 10)
for i in range(100,9,-10):
    print(i)
else:
    print('Done')
#100 - 10 going down by 10)
'''
total=0
for i in range(1,101):
    total=total + i
    print(f'Total: {total}')
else:
    print('Done')
