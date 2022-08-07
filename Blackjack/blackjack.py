"""
BlackJack game. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import random
import os
from art import header


def clear():
    """
    Clear the console window.
    """
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'posix':
        _ = os.system('clear')


def deal_card(num_of_cards, hand_list):
    """
    Returns wrapped inside an already existing list the passed number of random cards in the deck.
    """
    cards = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    for _ in range(num_of_cards):
        hand_list.append(cards[random.randint(0, len(cards) - 1)])
    return hand_list


def score(hand_list):
    """
    Take a list of cards and return the calculated total score of the cards.
    """
    score_sum = sum(hand_list)
    if score_sum == 21 and len(hand_list) == 2:
        return 0
    if 11 in hand_list and score_sum > 21:
        hand_list.remove(11)
        hand_list.append(1)
    return sum(hand_list)


def compare(user_score, computer_score):
    """
    Compares the scores and returns the appropriate win/lose/draw statement.
    """
    if user_score == computer_score:
        return 'It\'s a draw!\n'
    elif computer_score == 0:
        return 'You lose! Computer has Blackjack!\n'
    elif user_score == 0:
        return 'You win! You have Blackjack!\n'
    elif user_score > 21:
        return 'You went over. You lose!\n'
    elif computer_score > 21:
        return 'Computer went over. You win!\n'
    elif user_score > computer_score:
        return 'You win!\n'
    else:
        return 'You lose!\n'


def game():
    """
    Main chunk of the game's code inside a function for recursion.
    """
    print(header)

    user_hand = []
    deal_card(2, user_hand)
    computer_hand = []
    deal_card(2, computer_hand)
    computer_score = score(computer_hand)
    user_score = score(user_hand)
    game_over = False

    while not game_over:
        print(f'\nYour cards: {user_hand}, current score: {user_score}')
        print(f'Computer\'s first card: {computer_hand[0]}\n')
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_wants_deal = input('   Type "deal" to get another card or type "pass" to pass: ')
            if user_wants_deal in ('deal', 'd'):
                user_hand = deal_card(1, user_hand)
                user_score = score(user_hand)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand = deal_card(1, computer_hand)
        computer_score = score(computer_hand)

    print(f'\nYour final hand: {user_hand}, final score {user_score}')
    print(f'Computer\'s final hand: {computer_hand}, final score {computer_score}\n')
    print(compare(user_score, computer_score))

    while input('   Do you want to play again? "Y" or "N": ') in ('yes', 'y'):
        clear()
        game()
    quit()


clear()
game()
