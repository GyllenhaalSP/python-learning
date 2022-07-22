"""
OOP Coffee Machine program based on the APPBrewery skeleton. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

while True:
    choice = input(f'What would you like? {menu.get_items()} ')
    if choice in 'off':
        quit()
    elif choice in ('report', 'r'):
        print('')
        cm.report()
        mm.report()
        print('')
    else:
        order = menu.find_drink(choice)
        if cm.is_resource_sufficient(order):
            print(f'\nIt\'s ${order.cost}.')
            if mm.make_payment(order.cost):
                cm.make_coffee(order)
