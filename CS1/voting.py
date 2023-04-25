can='y'
n=18

nat=input('Are you Canadian (Y/N): ')


if nat.upper()=='Y':
    age=int(input('Please Enter your age: '))
    if age<18:
        print('Sorry, you are not old enough to vote!')
    elif age>=18:
        print('Congratulations, you are old enough to vote!')
    else:
        print('That is not a valid number')
else:
    print('Sorry, you need to be Canadian to vote!')
