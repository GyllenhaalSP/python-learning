"""
Calculator Program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import os
from art import header


def clear():
    """
    Clear the console window.
    """
    os.system('cls||clear') if os.name in ('nt', 'posix') else print('\n'*100)


def add(n1: str, n2: str) -> int | float:
    """
    Adds n1 and n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        n1 = float(n1) if '.' in n1 else int(n1)
    if type(n2) is str:
        n2 = float(n2) if '.' in n2 else int(n2)
    return n1 + n2


def subtract(n1: str, n2: str) -> int | float:
    """
    Subtracts n1 from n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        n1 = float(n1) if '.' in n1 else int(n1)
    if type(n2) is str:
        n2 = float(n2) if '.' in n2 else int(n2)
    return n1 - n2


def multiply(n1: str, n2: str) -> int | float:
    """
    Multiply n1 for n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        n1 = float(n1) if '.' in n1 else int(n1)
    if type(n2) is str:
        n2 = float(n2) if '.' in n2 else int(n2)
    return n1 * n2


def divide(n1: str, n2: str) -> int | float:
    """
    Divides n1 by n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        n1 = float(n1) if '.' in n1 else int(n1)
    if type(n2) is str:
        n2 = float(n2) if '.' in n2 else int(n2)
    return n1 / n2


def modulus(n1: str, n2: str) -> int | float:
    """
    Returns the remainder of the division of n1 by n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        n1 = float(n1) if '.' in n1 else int(n1)
    if type(n2) is str:
        n2 = float(n2) if '.' in n2 else int(n2)
    return n1 % n2


def exponent(n1: str, n2: str) -> int | float:
    """
    Raises n1 to the potency of n2, checking and converting types accordingly.
    """
    if type(n1) is str:
        n1 = float(n1) if '.' in n1 else int(n1)
    if type(n2) is str:
        n2 = float(n2) if '.' in n2 else int(n2)
    return n1 ** n2


def percentage(n1: str, n2: str) -> int | float:
    """
    Returns the n2 percentage of n1, checking and converting types accordingly.
    """
    if type(n1) is str:
        n1 = float(n1) if '.' in n1 else int(n1)
    if type(n2) is str:
        n2 = float(n2) if '.' in n2 else int(n2)
    return n2 * (n1 / 100)


def sqrt(n1: str) -> int | float:
    """
    Returns the square root of n1, checking and converting types accordingly.
    """
    if type(n1) is str:
        n1 = float(n1) if '.' in n1 else int(n1)
    return n1 ** 0.5


def headers():
    """
    De-cluttering function. Prints the header and the info whenever needed.
    """
    print(f'{" CALCULATOR ".center(110, "*")}')
    print(header)
    print(f'{"*" * 110}')
    print('\nFor PERCENTAGES, the first number that is introduced is the percentage.\n')
    print('For SQUARE ROOTS, press enter key without entering anything when prompted to '
          'introduce the next number.\n')


def menu_formatting():
    """
    Formats the output of the operation symbols.
    """
    print('\n[', end='')
    print('] ['.join(list(SYMBOLS)), end='')
    print(' - √]\n')


def is_digit(number: str | int | float) -> bool:
    """
    Checks if the user input is a digit. Either an integer or a float.
    """
    try:
        float(number)
        return True
    except ValueError:
        return False


def inputs(operation=None, times=None) -> str:
    """
    Checks operation and number input to meet the requirements: str, int, float or sqrt.
    """
    if times == 1:
        num = input("What\'s the first number?: ")
    else:
        num = input("\nWhat\'s the next number?: ")
        if not num and operation in 'sqrt':
            return num
    while not is_digit(num):
        num = input(f'Invalid input {num}. Please enter a number: ')
    return num


def operations(operation_list: list) -> str:
    """
    Takes the operation list and checks it against the user input.
    """
    operation = input('Pick an operation from the line above: ').lower()
    while True:
        if operation in operation_list:
            return operation
        menu_formatting()
        operation = input(f'Invalid input {operation}. Pick an operation from the line above: ')


def results(op, operand1=None, operand2=None, result=None, result2=None, operand3=None, times=None):
    """
    De-cluttering function. Formats the data and prints results nicely according to operation.
    """
    if times == 1:
        if op == '%':
            print(f'\n{operand1} {op} {operand2} = {result}')
            print(f'\n{operand1} {op} {operand2} = {operand2} + {operand1}% ({result}) = {result + float(operand2)}')
            print(f'\n{operand1} {op} {operand2} = {operand2} - {operand1}% ({result}) = {float(operand2) - result}\n')
        elif op == 'sqrt':
            print(f'\n \u221A {operand1} = {result}\n')
        else:
            print(f'\n{operand1} {op} {operand2} = {result}\n')
    elif not times:
        if op == '%':
            print(f'\n{result} {op} {operand3} = {result2}')
            print(f'\n{result} {op} {operand3} = {operand3} + {result}% ({result2}) = {result2 + float(operand3)}')
            print(f'\n{result} {op} {operand3} = {operand3} - {result}% ({result2}) = {float(operand3) - result2}\n')
        else:
            print(f'\n{result} {op} {operand3} = {result2}\n')


def keep_calc(result: int | float) -> bool:
    """
    Dialog to keep calculating with the previous number.
    """
    while True:
        choice = input(f'Do you want to keep calculating with {result}?\n{(chr(9))*7} "y" or "n": ').lower()
        match choice:
            case 'y' | 'yes':
                return True
            case 'n' | 'no':
                re_calc()
            case _:
                print(f'Invalid option: {choice}')


def re_calc():
    """
    Dialog to restart the calculator.
    """
    while True:
        choice = input('\nDo you want to start a new calculation?\n\n"Yes" to start a new '
                       'calculator:\n\n"No" to exit entirely: ').lower()
        match choice:
            case 'y' | 'yes':
                clear()
                calculator()
            case 'n' | 'no':
                quit()
            case _:
                print(f'\nInvalid option: {choice}')


def calculator():
    """
    Doesn't take any arguments. Simply used for recursion.
    """
    clear()
    headers()
    num1 = inputs(times=1)
    menu_formatting()
    operation = operations(OPERATION_LIST)
    num2 = inputs(operation=operation)
    calculation = SYMBOLS[operation]
    result = calculation(num1) if operation == 'sqrt' else calculation(num1, num2)
    results(operation, operand1=num1, operand2=num2, result=result, times=1)

    if keep_calc(result):
        print(f'Calculation result is {result}\n')

    while True:
        menu_formatting()
        operation = operations(OPERATION_LIST)
        num3 = inputs(operation=operation)
        calculation = SYMBOLS[operation]
        result2 = calculation(result, num3)
        results(operation, operand3=num3, result=result, result2=result2)
        result = result2
        if keep_calc(result2):
            print('')
        else:
            print(f'\nCalculation result is {result2}')
            re_calc()


SYMBOLS = {
        '+':    add,
        '-':    subtract,
        '*':    multiply,
        '/':    divide,
        'mod':  modulus,
        '^':    exponent,
        '%':    percentage,
        'sqrt': sqrt,
}

OPERATION_LIST = ['+', '-', '*', '/', 'mod', '^', '%', 'sqrt']

if __name__ == '__main__':
    calculator()
