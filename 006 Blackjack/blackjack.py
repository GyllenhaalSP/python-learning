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
    os.system('cls||clear') if os.name in ('nt', 'posix') else print('\n' * 100)


def deal_card(num_of_cards: int, hand: list) -> list:
    """
    Returns, wrapped inside an already existing list, the passed number of random cards in the deck.
    """
    cards = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    hand.extend(cards[random.randint(0, len(cards) - 1)] for _ in range(num_of_cards))

    return hand


def score(hand: list) -> int:
    """
    Take a list of cards and return the total score of the cards. If the user has blackjack in the first
    hand, it returns 0 to flag blackjack.
    """
    if (score_sum := sum(hand)) == 21 and len(hand) == 2:
        return 21
    if 11 in hand and score_sum > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def computer_hand_deal(computer_hand: list, computer_score: int) -> (list, int):
    """
    Keeps dealing cards to the computer until the conditions are met, so the values are sent for comparison.
    """
    while computer_score != 0 and computer_score < 17:
        computer_hand = deal_card(1, computer_hand)
        computer_score = score(computer_hand)
    return computer_hand, computer_score


def compare(user_score: int, computer_score: int) -> str:
    """
    Compares the scores and returns the appropriate win/lose/draw statement.
    """
    if user_score == computer_score:
        return 'It\'s a draw!\n'
    elif computer_score == 21:
        return 'You lose! Computer has Blackjack!\n'
    elif user_score == 21:
        return 'You win! You have Blackjack!\n'
    elif user_score > 21:
        return 'You went over. You lose!\n'
    elif computer_score > 21:
        return 'Computer went over. You win!\n'
    elif user_score > computer_score:
        return 'You win!\n'
    else:
        return 'You lose!\n'


def replay():
    """
    Triggers the replay dialog.
    """
    while choice := input('   Do you want to play again? "Y" or "N": ').lower():
        match choice:
            case 'y' | 'yes':
                clear()
                game()
            case 'n' | 'no':
                quit()
            case _:
                print(f'\nInvalid option: {choice}')


def game():
    """
    Main function for recursion.
    """
    print(header)

    deal_card(2, user_hand := [])
    deal_card(2, computer_hand := [])
    computer_score = score(computer_hand)
    user_score = score(user_hand)

    while True:
        print(f'\nYour cards: {user_hand}, current score: {user_score}')
        print(f'Computer\'s first card: {computer_hand[0]}\n')
        if user_score == 0 or computer_score == 0 or user_score > 21:
            break
        if input('   Type "deal" to get another card or type "pass" to pass: ') not in ('deal', 'd'):
            break
        user_hand = deal_card(1, user_hand)
        user_score = score(user_hand)

    if user_score == 0:
        user_score = 21
    elif computer_score == 0:
        computer_score = 21

    computer_hand, computer_score = computer_hand_deal(computer_hand, computer_score)

    print(f'\nYour final hand: {user_hand}, final score {user_score}')
    print(f'Computer\'s final hand: {computer_hand}, final score {computer_score}\n')
    print(compare(user_score, computer_score))

    replay()


if __name__ == '__main__':
    clear()
    game()
