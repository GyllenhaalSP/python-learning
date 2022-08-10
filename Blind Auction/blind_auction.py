"""
Blind Auction Program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import os
from art import header


def clear():
    """
    Clear the console window.
    """
    os.system('cls||clear') if os.name in ('nt', 'posix') else print('\n'*100)


def print_header():
    """
    Prints the header where needed.
    """
    print(header)
    print(' Welcome to the Secret Auction Program '.center(108, '*'), '\n')


def bidders_info_dict(bidder_name: str, bidder_price: int):
    """
    Updates dictionary populating it with the data the user inputs.
    """
    if bidder_name in data_dict.keys():
        bidder_name_numeric_augment = f'{bidder_name} {str(0) if bidders_info_dict.counter < 10 else ""}' \
                                      f'{str(bidders_info_dict.counter)}'
        data_dict.update({bidder_name_numeric_augment: bidder_price})
        bidders_info_dict.counter += 1
    data_dict.update({bidder_name: bidder_price})


def find_highest(info_dict: dict) -> list:
    """
    Find and returns the passed dictionary's highest value by key.
    """
    return [k for k, v in info_dict.items() if v == max(info_dict.values())]


data_dict = {}
bidders_info_dict.counter = 0

while True:
    print_header()
    name = input('What is your name?: ')
    while True:
        bid = input('What is your bid?: ')
        if bid.isdigit():
            break
        print(f'Introduce a numeric bid. Not {bid}.')
    bid = int(bid)
    bidders_info_dict(name, bid)
    while True:
        more_bidders = input('Are there any other bidders? Type "yes" or "no".\n')
        if more_bidders in ('yes', 'y', 'no', 'n'):
            break
        print(f'Invalid input: {more_bidders}')

    if more_bidders in ('yes', 'y'):
        clear()
        continue
    if more_bidders in ('no', 'n'):
        clear()
        break

highest_bidder = find_highest(data_dict)
print_header()
if len(highest_bidder) == 1:
    print(f'{"".join(highest_bidder)} is the highest bidder with {data_dict[highest_bidder[0]]}€!')
else:
    print(f'{", ".join(list(highest_bidder[:-1]))} and {highest_bidder[-1]} are the highest bidders with '
          f'{data_dict[highest_bidder[0]]}€!')
