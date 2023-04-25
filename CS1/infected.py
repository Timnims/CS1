day=1
inf=1
total=1

print(f'Day {day}')
print(f'Total infected: {total}\n')
while True:
    day=day+1
    print(f'Day {day}')
    inf=inf*2
    total=total+inf
    print(f'Total infected: {total}\n')
#    if total >= 8000000000:
#      break
