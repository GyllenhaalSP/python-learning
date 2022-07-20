"""
Calculator Program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import os
from art import header


def clear():
    """
    Clear the console window
    """
    if os.name == 'nt':
        _ = os.system('cls')


def add(n1, n2):
    """
    Adds n1 and n2
    """
    return n1 + n2


def subtract(n1, n2):
    """
    Subtracts n1 from n2
    """
    return n1 - n2


def multiply(n1, n2):
    """
    Multiply n1 for n2
    """
    return n1 * n2


def divide(n1, n2):
    """
    Divides n1 by n2
    """
    return n1 / n2


def menu_formatting():
    """
    Formats the output of the 'for' loop containing the operation symbols.
    """
    print('')
    print('[', end='')
    print('] ['.join([symbol for symbol in symbols]), end='')
    print(']')
    print('')


def calculator():
    """
    Doesn't take any arguments. Simply used for recursion.
    """
    clear()
    print(f'{" CALCULATOR ".center(104, "*")}')
    print(header)
    num1 = float(input('What\'s the first number?: '))
    menu_formatting()
    operation = input('Pick an operation from the line above: ')
    while True:
        if operation not in operations:
            menu_formatting()
            operation = input('Invalid input. Pick an operation from the line above: ')
            continue
        else:
            break
    num2 = input('\nWhat\'s the next number?: ')
    calculation = symbols[operation]
    result = calculation(num1, num2)
    print(f'\n{num1} {operation} {num2} = {result}\n')
    if input(f'Do you want to keep calculating with {result}?\n"y" or "n": ') == 'n':
        print(f'\nCalculation result is {result}\n')
        while True:
            choice = input('Do you want to start a new calculation?\n "y" to start a new '
                           'calculator or "n" to exit entirely: ')
            if choice == 'y':
                clear()
                calculator()
            elif choice == 'n':
                quit()
            else:
                print('\nInvalid input: Please enter "y" or "n".\n')
                continue
    else:
        while True:
            menu_formatting()
            operation = input('Pick another operation: ')
            while True:
                if operation not in operations:
                    menu_formatting()
                    operation = input('Invalid input. Pick another operation: ')
                    continue
                else:
                    break
            num3 = input('\nWhat\'s the next number?: ')
            print('')
            calculation = symbols[operation]
            result2 = calculation(result, num3)
            print(f'{result} {operation} {num3} = {result2}\n')
            result = result2
            if input(f'Do you want to keep calculating with {result2}?\n"y" or "n": ') == 'y':
                print('')
                continue
            else:
                print(f'\nCalculation result is {result2}')
                print('')
                if input('Do you want to start a new calculation?\n'
                         ' "y" to start a new calculator or "n" to exit entirely: ') == 'y':
                    clear()
                    calculator()
                else:
                    quit()


symbols = {
        '+':   add,
        '-':   subtract,
        '*':   multiply,
        '/':   divide,
}

operations = ['+', '-', '*', '/', 'mod', '^', '%']

calculator()
