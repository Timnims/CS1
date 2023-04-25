change=float(input('Insert total price: '))
change=change % 1
money=float(change)
money=int(money)
money=(money+1)-change

if money >= 0.25:
    quarter = money // 0.25
    money = round(money - (quarter * 0.25), 2)
    
    print(f'{quarter} quarter')
else:
    print('0 quarters')

if money >= 0.10:
    dime = money // 0.10
    money = round(money - (dime * 0.10), 2)
    
    print(f'{dime} dimes')
else:
    print('0 dimes')

if money >= 0.05:
    nickel = money // 0.05
    money = round(money - (nickel * 0.05), 2)
    
    print(f'{nickel} nickels')
else:
    print('0 nickels')

if money >= 0.01:
    penny = money // 0.01
    money = round(money - (penny * 0.01), 2)
    
    print(f'{penny} pennies')
else:
    print('0 pennies')
