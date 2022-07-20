"""
Hangman game by GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import random
import os
from art import header_en, HANGMANPICS


def clear():
    """
    Clear the console window
    """
    if os.name == 'nt':
        _ = os.system('cls')


def get_word(archive):
    """
    Retrieves a word from the word_list.txt file where all the words eligible for the game are stored.
    """
    with open(f'{archive}.txt', 'r') as word_list:
        data = word_list.read()
        words = data.split()

    random_word = random.choice(words)
    word_list.close()
    return random_word


print(header_en)
# Print initial gallows
print(f'{HANGMANPICS[7]}\n')

lives = 7
chosen_word = get_word('word_list')

# Line for debug purposes
print(f'Debug statement: {chosen_word}')

# Create blanks
guess = ''
display = []
repeats = []

for letter in chosen_word:
    display.append('_')

print(f'\n{" ".join(display)}\n')

while '_' in display:

    guess = input('Guess a letter, please: ').lower()

    while True:
        if not guess:
            guess = input('Nothing was inputted, please input a letter: ').lower()
            continue
        else:
            break

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
        print('You are hanging from the gallows. You "noose"!')
        break

    if '_' not in display:
        print('The gallows are empty again. You won!')
        print(f'{HANGMANPICS[7]}\n')
