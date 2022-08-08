"""
Guess the Number game. By GyllenhaalSP @ https://github.com/GyllenhaalSP.
"""
import os
import random
import time
from art import header, heart, broken


def clear():
    """
    Clear the console window.
    """
    os.system('cls||clear') if os.name in ('nt', 'posix') else print('\n'*100)


def lives(amount):
    """
    Calculate remaining lives and assign unicode hearts/broken hearts from art file accordingly.
    """
    hearts = heart * amount
    if amount == 0:
        hearts = broken
    return hearts


def validate_difficulty(difficulty):
    """
    Validate difficulty choice and triggers the set_difficulty function.
    If input is invalid it keeps asking for valid input.
    """
    while True:
        if difficulty in ('easy', 'e'):
            return set_difficulty('\nDifficulty set to EASY.', 10)
        elif difficulty in ('hard', 'h'):
            return set_difficulty('\nDifficulty set to HARD.', 5)
        elif difficulty in ('extra', 'extra-hard', 'extra hard', 'ex'):
            return set_difficulty('\nDifficulty set to EXTRA-HARD.', 3)
        difficulty = input('Invalid input. Please type "easy", "hard" or "extra-hard": ').lower()
        continue


def set_difficulty(diff_text, diff_lvl):
    """
    Return difficulty level and print difficulty text.
    """
    print(diff_text)
    return diff_lvl


def validate_digit(digit):
    """
    Validates user input and transforms it to INT or keeps asking for a valid input.
    """
    while True:
        if str.isdecimal(digit):
            return int(digit)
        digit = input('Invalid input. Please make a numeric guess: ')
        continue


def replay(option):
    """
    Checks user answer and routes the replay options. Keeps asking for correct input.
    """
    if option in ('y', 'yes'):
        clear()
        game()
    elif option in ('n', 'no'):
        return
    else:
        while True:
            option = input('Invalid input. "y" to play again or "n" to exit: ')
            if option in ('y', 'yes'):
                clear()
                game()
            elif option in ('n', 'no'):
                quit()
            continue


def hard_diff(difficulty, play):
    """
    Clears the screen after a 1.25-second delay and shows only the last guessed number.
    """
    if difficulty in ('hard', 'h'):
        time.sleep(1.25)
        clear()
        print(f'Your previous number was {play}')
        return


def extra_hard_diff(difficulty):
    """
    Clears the screen after a 0.75-second delay and doesn't show any info.
    """
    if difficulty in ('extra', 'extra-hard', 'ex'):
        time.sleep(0.75)
        clear()
        return


def game():
    """
    Main function for recursion.
    """
    clear()
    print(header)
    print('Welcome to the Number Guessing Game!\n')
    print(f'EASY mode gives you {heart * 10} lives. \n'
          f'HARD mode gives you {heart * 5} lives and wipes the previous screen.\n'
          f'EXTRA HARD mode gives you {heart * 3} lives and wipes your previous guesses.\n')
    print('Computer says:\n'
          '         I\'m thinking (do we think?) of a number between 1 and 100.\n')
    difficulty = input('Choose a difficulty. Type "easy", "hard" or "extra-hard": ').lower()
    counter = validate_difficulty(difficulty)
    num = random.randint(0, 100)

    while True:
        extra_hard_diff(difficulty)
        print(f'\nYou have {lives(counter)} lives remaining.\n')
        play = input('Make a guess: ')

        play = validate_digit(play)

        if counter < 2:
            print(f'\nYou ran out of lives! {broken}')
            print('I\'m sorry, you lose!')
            print(f'The number was {num}\n')
            again = input('Do you want to play again? "y" to play or "n" to exit: ')
            replay(again)

        elif play > num:
            print('Too high.')
            print('Guess Again!')
            counter -= 1
            hard_diff(difficulty, play)
            extra_hard_diff(difficulty)
            continue

        elif play < num:
            print('Too low.')
            print('Guess again!')
            counter -= 1
            hard_diff(difficulty, play)
            extra_hard_diff(difficulty)
            continue

        elif play == num:
            print('Congrats! You got it!')
            print(f'You finished with {lives(counter)} lives left!\n')
            again = input('Do you want to play again? "y" to play or "n" to exit: ')
            replay(again)


game()
