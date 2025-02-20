import random

while True:
    player = (input('select rock, paper, or scissors: '))

    selections = ['rock', 'paper', 'scissors']
    bot = random.choice(selections)
    print(f' the bot selected {bot}')

    if bot == 'rock' and player == 'paper':
        print('you win!')
    elif bot == 'rock' and player == 'scissors':
        print('You lose')
    elif bot == 'paper' and player == 'scissors':
        print('you win!')
    elif bot == 'paper' and player == 'rock':
        print('you lose')
    elif bot == 'scissors' and player =='rock':
        print('you win!')
    elif bot == 'scissors' and player == 'paper':
        print('You lose')
    else:
        print('its a Tie!')
    again = int(input('type 1 if ypu wish to play again, type 2 if you wish to exit: '))
    if again == 1:
        continue
    else:
        print('goodbye')
        break