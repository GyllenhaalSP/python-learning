"""
Blind Auction Program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import os
from art import header


def clear():
    """
    Clear the console window
    """
    if os.name == 'nt':
        _ = os.system('cls')


def bidders_info_dict(data, price):
    """
    Updates dictionary populating it with the data the user inputs.
    """
    new = {data: price}
    info.update(new)


def find_highest(info_dict):
    """
    Find and returns the passed dictionary's highest value by key.
    """
    highest = max(info_dict, key=info_dict.get)
    return highest


print(header)
print(f' Welcome to the Secret Auction Program '.center(108, '*'), '\n')

info = {}

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

highest_bidder = find_highest(info)

print(f'{highest_bidder} is the highest bidder with {info[highest_bidder]} €!')
