import os
import random
import sys
import time
from art import *


def clear():
    """
    Clear the console window.
    """
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'posix':
        _ = os.system('clear')


def lives(amount):
    """
    Calculate remaining lives and assign unicode hearts from art file accordingly.
    """
    hearts = heart * amount
    if amount == 0:
        hearts = broken
    return hearts


def game():
    """
    Wrapped code in function for recursion.
    """
    clear()
    print(header)
    print('Welcome to the Number Guessing Game!\n')
    print(f'Easy mode gives you {heart * 10} lives. \n'
          f'Hard mode gives you {heart * 5} lives and wipes the previous screen.\n'
          f'Extra Hard mode gives you {heart * 3} lives and wipes your previous guesses.\n')
    difficulty = input('Choose a difficulty. Type "easy", "hard" or "extra-hard": ').lower()

    while True:
        if difficulty in ('easy', 'e'):
            print('\nDifficulty set to EASY.')
            counter = 10
            break
        elif difficulty in ('hard', 'h'):
            print('\nDifficulty set to HARD.')
            counter = 5
            break
        elif difficulty in ('extra', 'extra-hard', 'extra hard', 'ex'):
            print('\nDifficulty set to EXTRA-HARD.')
            counter = 3
            break
        else:
            difficulty = input('Invalid input. Please type "easy", "hard" or "extra-hard": ').lower()
            continue

    print('\nI\'m thinking of a number between 1 and 100.')
    num = random.randint(0, 100)

    while True:
        print(f'\nYou have {lives(counter)} lives remaining.\n')
        play = input('Make a guess: ')
        while True:
            if str.isdecimal(play):
                play = int(play)
                break
            else:
                play = input('Invalid input. Please make a numeric guess: ')
                continue
        if counter < 2:
            print(f'\nYou ran out of lives! {broken}')
            print('I\'m sorry, you lose!\n')
            again = input('Do you want to play again? "y" to play or "n" to exit: ')
            if again in ('y', 'yes'):
                clear()
                game()
                break
            elif again in ('n', 'no'):
                sys.exit('END')
            else:
                while True:
                    again = input('Invalid input. "y" to play again or "n" to exit: ')
                    if again in ('y', 'yes'):
                        clear()
                        game()
                        break
                    elif again in ('n', 'no'):
                        sys.exit('END')
                    continue
        elif play > num:
            print('Too high.')
            print('Guess Again!')
            counter -= 1
            if difficulty in ('hard', 'h'):
                time.sleep(2)
                clear()
                print(f'Your previous number was {play}')
                continue
            if difficulty in ('extra', 'extra-hard', 'ex'):
                time.sleep(1)
                clear()
                continue
            continue
        elif play < num:
            print('Too low.')
            print('Guess again!')
            counter -= 1
            if difficulty in ('hard', 'h'):
                time.sleep(2)
                clear()
                print(f'Your previous number was {play}')
                continue
            if difficulty in ('extra', 'extra-hard', 'ex'):
                time.sleep(1)
                clear()
                continue
            continue
        elif play == num:
            print('Congrats! You got it!')
            print(f'You had {lives(counter)} lives left!\n')
            again = input('Do you want to play again? "y" to play or "n" to exit: ')
            if again == 'y':
                clear()
                game()
                break
            else:
                sys.exit('END')


game()
