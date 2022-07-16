import random
import os
from hangman_stages import *
from hangman_words import *


def clear():
    """
    Clear the console window
    """
    if os.name == 'nt':
        _ = os.system('cls')


print(hangman_logo)

lives = 7

# Initial gallows
print(f'{HANGMANPICS[7]}\n')

chosen_word = random.choice(word_list)
print(chosen_word)

# Create blanks
guess = ''
display = []
repeats = []

for letter in chosen_word:
    display.append('_')

while '_' in display:

    guess = input('Guess a letter, please: ').lower()
    clear()

    while True:
        if len(guess) > 1:
            print('\nYou\'ve introduced more than one letter\n')
            guess = input('Guess a letter, please: ').lower()
            continue
        if guess in repeats:
            print(f'You have already guessed {guess}\n')
            guess = input('Guess another letter, please: ').lower()
            continue
        if guess not in repeats:
            break

    # Check guessed letter
    for count, letters in enumerate(chosen_word):
        if guess in letters:
            display.pop(count)
            display.insert(count, guess)

    if guess in chosen_word:
        repeats.append(guess)
        guess = ''

    if guess not in chosen_word:
        repeats.append(guess)
        print(f'\n{guess} is not in the word.')
        lives -= 1

    print(f'\n{" ".join(display)}\n')

    if 1 <= lives <= 6:
        print(f'{HANGMANPICS[lives]}\n')

    if lives == 0:
        print(f'{HANGMANPICS[0]}\n')
        print('You lose!')
        break

    if '_' not in display:
        print(f'{HANGMANPICS[7]}\n')
        print('You won!')
