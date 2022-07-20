"""
Higher or Lower game. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import random
import os
from art import header, vs
from game_data import data


def clear():
    """
    Clear the console window
    """
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'posix':
        _ = os.system('clear')


def random_contestant():
    """
    Chooses randomly a contestant.
    """
    contestant = random.choice(data)
    index = data.index(contestant)
    return index


def repeat_choice(repeat, index_value):
    """
    Takes the repeat value and the index value to compare and if the game is already on a repetition, it returns
    the previous index value. Else, it returns a new one.
    """
    if repeat == 1:
        return index_value
    else:
        return random_contestant()


def check_choice(choice, score, a, b):
    """
    Checks user choice, passing the indexes in order to compare them.
    """
    def losing():
        """
        Unifies the else statements.
        """
        clear()
        print(f'You lose! Your score was {score}')
        repeat = input('Do you want to play again? Type "y" or "n": ')
        while True:
            if repeat in ('yes', 'y'):
                game(0, 0, None)
            elif repeat in ('no', 'n'):
                quit()
            else:
                repeat = input('\nInvalid input. Type "y" to play again or "n" to exit: ')
                continue

    if data[a][foll_count] == data[b][foll_count]:
        if choice in ('a', 'b'):
            print('They are equal!')
            score += 0
            game(score, 1, None)
    elif data[a][foll_count] > data[b][foll_count]:
        if choice in 'a':
            print('Great job!')
            score += 1
            game(score, 1, b)
        else:
            losing()

    elif data[b][foll_count] > data[a][foll_count]:
        if choice in 'b':
            print('Great job!')
            score += 1
            game(score, 1, a)
        else:
            losing()


def game(score, repeat, index_value):
    """
    Takes the score (initial = 0), the repeat status (0 = first occurrence, 1 = repeated game) and the index value
    of the previous "lower" index (the one that loses in the comparison). Then it keeps a recursive loop inside itself
    to keep the game going, passing the same arguments but updated.
    """
    clear()
    print(header)

    if score > 0:
        print(f'Well done! Your current score is {score}.\n')

    index_a = repeat_choice(repeat, index_value)
    index_b = repeat_choice(repeat, index_value)

    while True:
        if index_a == index_b:
            index_b = random_contestant()
            continue
        else:
            break

    print(f'Contestant A\n\n{data[index_a][name].upper()}, {data[index_a][desc]}, from {data[index_a][country]}')
    print(vs)
    print(f'{data[index_b][name].upper()}, {data[index_b][desc]}, from {data[index_b][country]}\n\nContestant B')

    choice = input('\nWho has more followers? Type "A" or "B": ').lower()

    while True:
        if choice in ("a", "b"):
            break
        else:
            choice = input('\nInvalid input. Choose "A" or "B": ').lower()
            continue

    check_choice(choice, score, index_a, index_b)


name, foll_count, desc, country = ('name', 'follower_count', 'description', 'country')

game(0, 0, None)
