"""
Coffee Machine program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources(user_choice):
    """
    Checks the machine stock against the user order.
    """
    if user_choice in ('latte', 'l'):
        if resources['water'] < 200 or resources['milk'] < 150 or resources['coffee'] < 24:
            print('\nSorry, not enough resources.\n')
            return False
        else:
            return True
    if user_choice in ('cappuccino', 'c'):
        if resources['water'] < 250 or resources['milk'] < 100 or resources['coffee'] < 24:
            print('\nSorry, not enough resources.\n')
            return False
        else:
            return True
    elif user_choice in ('espresso', 'e'):
        if resources['water'] < 50 or resources['coffee'] < 18:
            print('\nSorry, not enough resources.\n')
            return False
        else:
            return True


def coin_processing():
    """
    Ask for the coins and return the total introduced.
    """
    print('\nPlease, insert coins.')
    total = int(input('\nHow many pennies? ')) * PENNY
    total += int(input('How many nickels? ')) * NICKEL
    total += int(input('How many dimes? ')) * DIME
    total += int(input('How many quarters? ')) * QUARTER
    return total


def statistics_final_balance(user_choice, price_paid):
    """
    Deduces successfully spent resources from choice and updates money won with transaction.
    """
    if user_choice in ('espresso', 'e'):
        resources['money'] += price_paid
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    elif user_choice in ('latte', 'l'):
        resources['money'] += price_paid
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    elif user_choice in ('cappuccino', 'c'):
        resources['money'] += price_paid
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']


while True:
    choice = input('What would you like?\n(espresso/latte/cappuccino) ')

    if choice in ('espresso', 'e'):
        if check_resources(choice):
            money_inserted = coin_processing()
            price = MENU['espresso']['cost']
            if price > money_inserted:
                if money_inserted <= 0:
                    print('\nSorry, no money inserted.\n')
                else:
                    print('Sorry, not enough money inserted. Money refunded.\n')
                continue
            elif price <= money_inserted:
                change = money_inserted - price
                if change > 0:
                    print(f'\nHere is ${change:0.2f} in change.\n')
                else:
                    print(f'\nNo change.\n')
                statistics_final_balance(choice, price)
                print('Here is your espresso. Enjoy!\n')
                continue
        else:
            continue
    elif choice in ('latte', 'l'):
        if check_resources(choice):
            money_inserted = coin_processing()
            price = MENU['latte']['cost']
            if price > money_inserted:
                if money_inserted <= 0:
                    print('\nSorry, no money inserted.\n')
                else:
                    print('Sorry, not enough money inserted. Money refunded.\n')
                continue
            elif price <= money_inserted:
                change = money_inserted - price
                if change > 0:
                    print(f'\nHere is ${change:0.2f} in change.\n')
                else:
                    print(f'\nNo change.\n')
                statistics_final_balance(choice, price)
                print('Here is your latte. Enjoy!\n')
                continue
        else:
            continue
    elif choice in ('cappuccino', 'c'):
        if check_resources(choice):
            money_inserted = coin_processing()
            price = MENU['cappuccino']['cost']
            if price > money_inserted:
                if money_inserted <= 0:
                    print('\nSorry, no money inserted.\n')
                else:
                    print('Sorry, not enough money inserted. Money refunded.\n')
                continue
            elif price <= money_inserted:
                change = money_inserted - price
                if change > 0:
                    print(f'\nHere is ${change:0.2f} in change.\n')
                else:
                    print(f'\nNo change.\n')
                statistics_final_balance(choice, price)
                print('Here is your cappuccino. Enjoy!\n')
                continue
        else:
            continue
    elif choice in ('report', 'r'):
        print("")
        for key, value in resources.items():
            if key in ('milk', 'water'):
                print(f'{key.capitalize()}: {value}ml')
            elif key in 'coffee':
                print(f'{key.capitalize()}: {value}g')
            elif key in 'money_profit':
                print(f'{key.capitalize()}: ${value}')
        print("")
        continue
    elif choice in 'off':
        quit()
