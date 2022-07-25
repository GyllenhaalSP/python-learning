"""
Caesar Cipher program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import os
import locale
from art import header_en, header_es


def clear():
    """
    Clear the console window
    """
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'posix':
        _ = os.system('clear')


def get_lang():
    """
    Gets the user OS language
    """
    if os.name != 'posix':
        return locale.getdefaultlocale()
    elif os.name == 'posix':
        return os.getenv('LANG')


def caesar(lang, message, shift_amount, cipher_direction):
    """
    Receives the message to cipher and applies the shift_amount and cipher_direction chosen by the user.
    """
    alph_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z']
    alph_es = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó', 'p',
               'q', 'r', 's', 't', 'u', 'ú', 'ü', 'v', 'w', 'x', 'y', 'z']
    rejoined = []
    alphabet_len = 0
    split = [char for char in message]

    if cipher_direction in ('decode', 'dec', 'd', 'descodificar', 'des'):
        shift_amount *= -1

    if lang in 'es':
        alphabet_len = len(alph_es)
    elif lang in 'en':
        alphabet_len = len(alph_en)

    for char in split:
        if lang in 'es':
            if char not in alph_es:
                rejoined.append(char)
                continue
            index = alph_es.index(char) + shift_amount
            if index >= alphabet_len:
                index -= alphabet_len
            elif index < 0:
                index += alphabet_len
            rejoined.append(alph_es[index])
        elif lang in 'en':
            if char not in alph_en:
                rejoined.append(char)
                continue
            index = alph_en.index(char) + shift_amount
            if index >= alphabet_len:
                index -= alphabet_len
            elif index < 0:
                index += alphabet_len
            rejoined.append(alph_en[index])
    cipher_text = ''.join(rejoined)
    if cipher_direction in ('encode', 'enc', 'e', 'codificar', 'cod', 'c'):
        if lang in 'es':
            return f'\nEl texto codificado es: {cipher_text.capitalize()}\n'
        elif lang in 'en':
            return f'\nThe encoded text is: {cipher_text.capitalize()}\n'
    elif cipher_direction in ('decode', 'dec', 'd', 'descodificar', 'des'):
        if lang in 'es':
            return f'\nEl texto descodificado es: {cipher_text.capitalize()}\n'
        elif lang in 'en':
            return f'\nThe decoded text is: {cipher_text.capitalize()}\n'


def program():
    """
    Main program wrapped in a function for recursion purposes.
    """
    lang = get_lang()
    lang = lang[0]

    if lang in ('en_GB', 'en_US'):
        lang = 'en'
        print(header_en)
    elif lang in 'es_ES':
        lang = 'es'
        print(header_es)
    else:
        print('Your language seems to be neither English nor Spanish. Defaulting to English.')
        lang = 'en'
        clear()
        print(header_en)

    if lang in 'es':
        while True:
            direction = input("Introduce 'codificar' para encriptar o 'descodificar' para desencriptar: ").lower()
            if direction in ('codificar', 'cod', 'c'):
                break
            elif direction in ('descodificar', 'desc', 'd'):
                break
            else:
                print('\nOpción no encontrada.')
                continue

        text = input("Introduce el mensaje: ").lower()
        shift = input("Introduce el número de espacios de desplazamiento: ")
        while True:
            if shift.isdigit():
                shift = int(shift)
                if shift > 30:
                    shift %= 31
                break
            else:
                shift = input('\nInput inválido. Por favor, introduce un número: ')
                continue

        print(caesar(lang, text, shift, direction))

        restart = input('¿Quieres volver a encriptar o desencriptar un mensaje? Teclea "Sí" o "No": ').lower()
        if restart in ('si', 'sí', 's'):
            clear()
            program()
        else:
            print('¡Adiós!')
            quit()

    elif lang in 'en':
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

        print(caesar(lang, text, shift, direction))

        restart = input('Do you want to go again? Type "Yes" or "No": ')
        if restart in ('yes', 'y'):
            clear()
            program()
        else:
            print('Goodbye')
            quit()


program()
