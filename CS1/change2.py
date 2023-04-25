mon=int(input('Enter Change: '))


q=mon//25
mon=mon % 25

d=mon//10
mon=mon % 10

n=mon//5
mon=mon % 5

p=mon//1

print(f'{q} Quarters')
print(f'{d} Dimes')
print(f'{n} Nickels')
print(f'{p} Pennies')
