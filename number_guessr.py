import random
import time
# TODO Create a simple number guessing game where the computer randomly selects a number between 1 and 100, and the player has to guess it. 
# TODO The program should provide feedback on whether the guess is too high, too low, or correct.

number = random.randint(1,100)
tries = 0
while True:
    player = int(input('Please enter a number: '))
    if player < number:
        print('your number is to low, try higher')
        tries+=1
    elif player > number:
        print('Your number is to high, try lower')
        tries+=1
    else:
        tries+=1
        print(f'correct! the number was {number}, you guessed in {tries} tries.')
        time.sleep(1)
        choice = int(input('type 1 to exit, type 2 to continue'))
        if choice == 1:
            print('Goodbye!')
            
            break
        else:
            number = random.randint(1,100)
            continue
