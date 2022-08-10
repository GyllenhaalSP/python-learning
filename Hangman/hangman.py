"""
Hangman game by GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import random
import os
from art import header_en, HANGMANPICS


def clear():
    """
    Clear the console window.
    """
    os.system('cls||clear') if os.name in ('nt', 'posix') else print('\n'*100)


def get_word(archive: str) -> str:
    """
    Retrieves a word from the txt file where all the words are stored.
    """
    with open(f'{archive}.txt', 'r') as word_list:
        data = word_list.read()
        words = data.split()

    random_word = random.choice(words)
    word_list.close()
    return random_word


def print_header():
    """
    Prints the header and the initial gallows.
    """
    print(header_en)
    print(f'{HANGMANPICS[7]}\n')


def guess_checker(guess: str, chosen_word: str,  displayed: list) -> list:
    """
    Checks the user guess against the chosen word from the word_list.
    """
    for index, chars in enumerate(chosen_word):
        if guess in chars:
            displayed.pop(index)
            displayed.insert(index, guess)
    print(f'\n{" ".join(displayed)}\n')
    return displayed


def repeats_checker(guess: str, repeats: list, lives: int, chosen_word: str) -> (str, list, int):
    """
    Checks repeated words and updates all values dependent on guess being a repeated word or not.
    """
    repeats.append(guess)
    if guess in chosen_word:
        ''
    else:
        print(f'\n{guess} is not in the word.')
        lives -= 1
    return guess, repeats, lives


def winning_conditions(lives: int, displayed: list, chosen_word: str) -> bool:
    """
    Checks the lives counter and the list containing the word chars and directs the next game stage.
    """
    if 1 <= lives <= 7:
        print(f'{HANGMANPICS[lives]}\n')
        return True
    elif lives == 0:
        print(f'{HANGMANPICS[0]}\n')
        print('You are hanging from the gallows. You "noose"!')
        print(f'The word was: {chosen_word}')
        return False
    elif '_' not in displayed:
        print('The gallows are empty again. You won!')
        print(f'{HANGMANPICS[7]}\n')
        return False


def replay():
    """
    Dialog to replay the game.
    """
    while True:
        choice = input('Do you want to play again? "Yes" or "No"?: ').lower()
        match choice:
            case 'y' | 'yes':
                clear()
                game()
            case 'n' | 'no':
                quit()
            case _:
                print(f'Invalid option: {choice}')


def game():
    """
    Main function for recursion.
    """
    print_header()
    chosen_word = get_word('word_list')

    # Line for debug purposes
    # print(f'Debug statement: {chosen_word}')

    lives = 7
    repeats = []
    displayed = ['_' for _ in chosen_word]
    print(f'\n{" ".join(displayed)}\n')

    while '_' in displayed:
        guess = input('Guess a letter, please: ').lower()

        match guess:
            case "":
                print('You have not introduced anything!\n')
                continue
            case guess if not guess.isalpha():
                print('WTF br0, I said LETTER...\n')
                continue
            case guess if len(guess) > 1:
                print(f'You\'ve introduced more than one letter: {guess}\n')
                continue
            case guess if guess in repeats:
                print(f'You have already guessed {guess}\n')
                continue

        displayed = guess_checker(guess, chosen_word, displayed)

        guess, repeats, lives = repeats_checker(guess, repeats, lives, chosen_word)

        winning_conditions(lives, displayed, chosen_word)

    replay()


if __name__ == '__main__':
    game()
