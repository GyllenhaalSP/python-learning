"""
Caesar Cipher program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import os
from art import *


def clear():
    """
    Clear the console window
    """
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'posix':
        _ = os.system('clear')


def caesar_en(message, shift_amount, cipher_direction):
    """
    Receives the message to cipher and applies the shift_amount and cipher_direction chosen by the user.
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']
    split = [char for char in message]
    rejoined = []
    alphabet_len = len(alphabet)
    if cipher_direction in ('decode', 'dec', 'd'):
        shift_amount *= -1
    for char in split:
        if char not in alphabet:
            rejoined.append(char)
            continue
        index = alphabet.index(char) + shift_amount
        if index >= alphabet_len:
            index -= alphabet_len
        elif index < 0:
            index += alphabet_len
        rejoined.append(alphabet[index])
    cipher_text = ''.join(rejoined)
    if cipher_direction in ('encode', 'enc', 'e'):
        return f'\nThe encoded text is: {cipher_text.capitalize()}\n'
    elif cipher_direction in ('decode', 'dec', 'd'):
        return f'\nThe decoded text is: {cipher_text.capitalize()}\n'


def program():
    """
    Main program wrapped in a function for recursion purposes.
    """
    print(header)
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        if direction in ('encode', 'enc', 'e'):
            break
        elif direction in ('decode', 'dec', 'd'):
            break
        else:
            print('\nNo such option')
            continue

    text = input("Type your message: ").lower()
    shift = input("Type the shift number: ")
    while True:
        if shift.isdigit():
            shift = int(shift)
            if shift > 25:
                shift %= 26
            break
        else:
            shift = input('\nInvalid input. Please introduce a number: ')
            continue

    print(caesar_en(text, shift, direction))

    restart = input('Do you want to go again? Type "Yes" or "No": ')
    if restart in ('yes', 'y'):
        clear()
        program()
    else:
        print('Goodbye')
        quit()


program()


