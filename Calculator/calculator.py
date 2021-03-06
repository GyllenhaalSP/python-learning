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
    Adds n1 and n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        if '.' in n1:
            n1 = float(n1)
        else:
            n1 = int(n1)

    if type(n2) is str:
        if '.' in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
    return n1 + n2


def subtract(n1, n2):
    """
    Subtracts n1 from n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        if '.' in n1:
            n1 = float(n1)
        else:
            n1 = int(n1)

    if type(n2) is str:
        if '.' in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
    return n1 - n2


def multiply(n1, n2):
    """
    Multiply n1 for n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        if '.' in n1:
            n1 = float(n1)
        else:
            n1 = int(n1)

    if type(n2) is str:
        if '.' in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
    return n1 * n2


def divide(n1, n2):
    """
    Divides n1 by n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        if '.' in n1:
            n1 = float(n1)
        else:
            n1 = int(n1)

    if type(n2) is str:
        if '.' in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
    return n1 / n2


def modulus(n1, n2):
    """
    Returns the remainder of the division of n1 by n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        if '.' in n1:
            n1 = float(n1)
        else:
            n1 = int(n1)

    if type(n2) is str:
        if '.' in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
    return n1 % n2


def exponent(n1, n2):
    """
    Raises n1 to the potency of n2, checking their type and converting them accordingly.
    """
    if type(n1) is str:
        if '.' in n1:
            n1 = float(n1)
        else:
            n1 = int(n1)

    if type(n2) is str:
        if '.' in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
    return n1 ** n2


def percentage(n1, n2):
    """
    Returns the n2 percentage of n1, checking their type and converting them accordingly.
    """
    if type(n1) is str:
        if '.' in n1:
            n1 = float(n1)
        else:
            n1 = int(n1)

    if type(n2) is str:
        if '.' in n2:
            n2 = float(n2)
        else:
            n2 = int(n2)
    return n2 * (n1 / 100)


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
    print(f'{" CALCULATOR ".center(110, "*")}')
    print(header)
    print('For percentages, the first number that it is introduced is the percentage.\n')

    num1 = input('What\'s the first number?: ')
    flag = True
    while flag:
        for char in num1:
            if char in valid_inputs:
                flag = False
            else:
                flag = True
                num1 = input('Invalid input. Please enter a number: ')
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
    flag = True
    while flag:
        for char in num2:
            if char in valid_inputs:
                flag = False
            else:
                flag = True
                num2 = input('Invalid input. Please enter a number: ')
    calculation = symbols[operation]
    result = calculation(num1, num2)
    if operation == '%':
        print(f'\n{num1} {operation} {num2} = {result}')
        print(f'\n{num1} {operation} {num2} = {num2} + {num1}% ({result}) = {result + float(num2)}')
        print(f'\n{num1} {operation} {num2} = {num2} - {num1}% ({result}) = {float(num2) - result}\n')
    else:
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
            if operation == '%':
                print(f'\n{result} {operation} {num3} = {result2}')
                print(f'\n{result} {operation} {num3} = {result2} + {result}% ({result2}) = {result2 + float(num2)}')
                print(f'\n{result} {operation} {num3} = {num3} - {result}% ({result2}) = {float(num3) - result2}\n')
            else:
                print(f'\n{result} {operation} {num3} = {result2}\n')
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
        'mod': modulus,
        '^':   exponent,
        '%':   percentage,
}

operations = ['+', '-', '*', '/', 'mod', '^', '%']
valid_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

calculator()
