'''
sen=input('Enter sentence: ')
words=0
for let in sen:
    if let in ' ':
        words=words+1
words=words+1
print(f'There are {words} words in "{sen}"')
'''
words=1
sen=input('Enter sentence: ').strip()

lastlet=' '
for let in sen:
    
    if let == ' ' and lastlet != ' ':
        words=words+1
    lastlet=let
print(f'There are {words} words')
