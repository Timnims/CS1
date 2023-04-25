import random
att=0


running=True

while running:
    running=True
    number=random.randrange(1,101)
    guesses=0
    while running:
        guesses=guesses+1
        guess=int(input('Guess a whole number between 1 and 100: '))
        

            
        if guess<number:
            print('Incorrect, try a higher number!\n')
            
        elif guess>number:
            print('Incorrect, try a lower number!\n')
            
        elif guess==number:
            print('Congratulations, you guessed the number!')
            print('GG, Thank you for playing!\n')
            print(f'It took you {guesses} guesses!\n')
            running=False
        
    play=input('Would you like to play again? (Y/N): ')
    if play.upper()=='N':
        print('Game Over')
        running=False
        
    elif play.upper()=='Y':                                                                           
        att=int(att)
        att=att+1
        print(f'Attempt {att+1}')
        running=True
    else:
        print('Invalid Input, Ending')

#Simple guess the number game
