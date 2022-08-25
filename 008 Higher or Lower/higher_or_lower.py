"""
Higher or Lower game. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import random
import os
from art import header, vs
from game_data import data

NAME, FOLL_COUNT, DESC, COUNTRY = ('name', 'follower_count', 'description', 'country')


def clear():
    """
    Clear the console window.
    """
    os.system('cls||clear') if os.name in ('nt', 'posix') else print('\n'*100)


def header_printer():
    """
    Prints the header
    """
    clear()
    print(header)


def random_contestant() -> int:
    """
    Chooses a contestant randomly.
    """
    contestant = random.choice(data)
    return data.index(contestant)


def repeat_choice(repeat: int, index_value: int | None) -> int | None:
    """
    Returns the previous index value if the game is already a repetition or else, it returns a new one.
    """
    return index_value if repeat == 1 else random_contestant()


def losing(score: int):
    """
    Unifies the game repeating options.
    """
    clear()
    print(f'You lose! Your score was {score}')
    repeat = input('Do you want to play again? Type "y" or "n": ').lower()
    while True:
        if repeat in {'yes', 'y'}:
            game(0, 0, None)
        elif repeat in {'no', 'n'}:
            quit()
        repeat = input('\nInvalid input. Type "y" to play again or "n" to exit: ').lower()


def check_choice(choice: str, score: int, a: int, b: int):
    """
    Checks user choice, passing the indexes in order to compare them.
    """
    if data[a][FOLL_COUNT] == data[b][FOLL_COUNT]:
        if choice in {'a', 'b'}:
            choice_router('They are equal!', 0, score, None)
    elif data[a][FOLL_COUNT] > data[b][FOLL_COUNT]:
        if choice in 'a':
            choice_router('Great job!', 1, score, b)
        losing(score)
    elif data[b][FOLL_COUNT] > data[a][FOLL_COUNT]:
        if choice in 'b':
            choice_router('Great job!', 1, score, a)
        losing(score)


def choice_router(message: str, repeat: int, score: int, index_value: int | None):
    """
    Routes the check_choice options.
    """
    print(message)
    score += repeat
    game(score, 1, index_value)


def game(score: int, repeat: int, index_value: int | None):
    """
    Takes the score (initial = 0), the repeat status (0 = first occurrence, 1 = repeated game) and the index value
    of the previous "lower" index (the one that loses in the comparison). Then it keeps a recursive loop inside itself
    to keep the game going, passing the same arguments but updated.
    """
    header_printer()

    if score > 0:
        print(f'Well done! Your current score is {score}.\n')

    index_a = repeat_choice(repeat, index_value)
    index_b = repeat_choice(repeat, index_value)

    while index_a == index_b:
        index_b = random_contestant()

    print(f'Contestant A\n\n{data[index_a][NAME].upper()}, {data[index_a][DESC]}, from {data[index_a][COUNTRY]}')
    print(vs)
    print(f'{data[index_b][NAME].upper()}, {data[index_b][DESC]}, from {data[index_b][COUNTRY]}\n\nContestant B')

    choice = input('\nWho has more followers? Type "A" or "B": ').lower()

    while choice not in ("a", "b"):
        choice = input('\nInvalid input. Choose "A" or "B": ').lower()

    check_choice(choice, score, index_a, index_b)


if __name__ == '__main__':

    game(0, 0, None)
