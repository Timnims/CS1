
sen=input('Enter sentence: ')
vowcount=0
#for let in sen:
for x in range(len(sen)):
   # if let in 'aeiou':
   if sen[x] in 'aeiou':
        vowcount= vowcount+1
print(f'There are {vowcount} vowels in: "{sen}"')

