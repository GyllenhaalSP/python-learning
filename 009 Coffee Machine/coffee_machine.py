"""
Coffee Machine program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25
NEMI = '\nSorry, no money inserted.\n'
NEMIR = 'Sorry, not enough money inserted. Money refunded.\n'
NOTISCHANGE = f'\nNo change.\n'

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


def check_resources(user_choice: str) -> bool:
    """
    Checks the machine stock against the user order.
    """
    if user_choice in {'latte', 'l'}:
        return check_milky_beverages(200, 150)
    if user_choice in {'cappuccino', 'c'}:
        return check_milky_beverages(250, 100)
    elif user_choice in {'espresso', 'e'}:
        if resources['water'] >= 50 and resources['coffee'] >= 18:
            return True
        print('\nSorry, not enough resources.\n')
        return False


def check_milky_beverages(water: int, milk: int) -> bool:
    """
    Checks the milky beverages resources.
    """
    if resources['water'] >= water and resources['milk'] >= milk and resources['coffee'] >= 24:
        return True
    print('\nSorry, not enough resources.\n')
    return False


def coin_processing() -> int:
    """
    Ask for the coins and return the total introduced.
    """
    print('\nPlease, insert coins.')
    total = int(input('\nHow many pennies? ')) * PENNY
    total += int(input('How many nickels? ')) * NICKEL
    total += int(input('How many dimes? ')) * DIME
    total += int(input('How many quarters? ')) * QUARTER
    return total


def statistics_final_balance(user_choice: str, price_paid: int | float):
    """
    Deduces successfully spent resources from choice and updates money won with transaction.
    """
    if user_choice in {'espresso', 'e'}:
        resource_updater(price_paid, 'espresso', 'coffee')
    elif user_choice in {'latte', 'l'}:
        resource_updater(price_paid, 'latte', 'milk')
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    elif user_choice in {'cappuccino', 'c'}:
        resource_updater(price_paid, 'cappuccino', 'milk')
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']


def resource_updater(price_paid: int | float, beverage: str, resource: str):
    """
    Updates the machine resources and money.
    """
    resources['money'] += price_paid
    resources['water'] -= MENU[beverage]['ingredients']['water']
    resources[resource] -= MENU[beverage]['ingredients'][resource]


while True:
    choice = input('What would you like?\n(espresso/latte/cappuccino) ')
    if not choice:
        continue
    if choice in ('espresso', 'e'):
        if not check_resources(choice):
            continue
        money_inserted = coin_processing()
        price = MENU['espresso']['cost']
        if price > money_inserted:
            if money_inserted <= 0:
                print(NEMI)
            else:
                print(NEMIR)
        else:
            change = money_inserted - price
            if change > 0:
                print(f'\nHere is ${change:0.2f} in change.\n')
            else:
                print(NOTISCHANGE)
            statistics_final_balance(choice, price)
            print('Here is your espresso. Enjoy!\n')
    elif choice in ('latte', 'l'):
        if check_resources(choice):
            money_inserted = coin_processing()
            price = MENU['latte']['cost']
            if price > money_inserted:
                if money_inserted <= 0:
                    print(NEMI)
                else:
                    print(NEMIR)
            else:
                change = money_inserted - price
                if change > 0:
                    print(f'\nHere is ${change:0.2f} in change.\n')
                else:
                    print(NOTISCHANGE)
                statistics_final_balance(choice, price)
                print('Here is your latte. Enjoy!\n')
    elif choice in ('cappuccino', 'c'):
        if check_resources(choice):
            money_inserted = coin_processing()
            price = MENU['cappuccino']['cost']
            if price > money_inserted:
                if money_inserted <= 0:
                    print(NEMI)
                else:
                    print(NEMIR)
            else:
                change = money_inserted - price
                if change > 0:
                    print(f'\nHere is ${change:0.2f} in change.\n')
                else:
                    print(NOTISCHANGE)
                statistics_final_balance(choice, price)
                print('Here is your cappuccino. Enjoy!\n')
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
    elif choice in 'off':
        quit()
