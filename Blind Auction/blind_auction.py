"""
Blind Auction Program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
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


def bidders_info_dict(bidder_name, bidder_price):
    """
    Updates dictionary populating it with the data the user inputs.
    """
    data_dict.update({bidder_name: bidder_price})


def find_highest(info_dict):
    """
    Find and returns the passed dictionary's highest value by key.
    """
    return max(info_dict, key=info_dict.get)


print(header)
print(' Welcome to the Secret Auction Program '.center(108, '*'), '\n')

data_dict = {}

while True:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: '))
    more_bidders = input('Are there any other bidders? Type "yes" or "no".\n')
    bidders_info_dict(name, bid)
    if more_bidders in ('yes', 'y'):
        clear()
        continue
    if more_bidders in ('no', 'n'):
        clear()
        break

highest_bidder = find_highest(data_dict)

print(f'{highest_bidder} is the highest bidder with {data_dict[highest_bidder]} €!')
