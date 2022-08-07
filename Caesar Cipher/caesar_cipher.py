"""
Caesar Cipher program. By GyllenhaalSP 2022 @ https://github.com/GyllenhaalSP.
"""
import os
import locale
from art import header_en, header_es


def clear():
    """
    Clear the console window.
    """
    if os.name == 'nt':
        _ = os.system('cls')
    elif os.name == 'posix':
        _ = os.system('clear')


def get_lang() -> str:
    """
    Gets the user OS language.
    Returns the first item in the (locale, codification) tuple returned by getdefaultlocale().
    """
    lang = locale.getdefaultlocale() if os.name != 'posix' else os.getenv('LANG')
    return lang[0]


def language_matching(lang: str) -> str:
    """
    Returns lang variable according to the results of the get_lang function.
    """
    match lang:
        case 'en_GB' | 'en_US':
            lang = 'en'
            print(header_en)
            return lang
        case 'es_ES':
            lang = 'es'
            print(header_es)
            return lang
        case _:
            print('Your language seems to be neither English nor Spanish. Defaulting to English.')
            lang = 'en'
            clear()
            print(header_en)
            return lang


def text_direction(language: str) -> str:
    """
    Returns user choice regarding ciphering direction in both languages.
    """
    while True:
        if language in 'es':
            direction = input("Introduce 'codificar' para encriptar o 'descodificar' para desencriptar: ").lower()
            if direction in ('codificar', 'cod', 'c', 'descodificar', 'desc', 'd'):
                return direction
            print('\nOpción no encontrada.\n')
            continue
        elif language in 'en':
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
            if direction in ('encode', 'enc', 'e', 'decode', 'dec', 'd'):
                return direction
            print('\nNo such option.\n')
            continue


def caesar(language: str, message: str, shift_amount: int, cipher_direction: str) -> str:
    """
    Receives the message to cipher and applies the shift_amount and cipher_direction chosen by the user.
    """
    alph_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z']
    alph_es = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó', 'p',
               'q', 'r', 's', 't', 'u', 'ú', 'ü', 'v', 'w', 'x', 'y', 'z']
    rejoined = []
    alphabet_len = 0
    split = list(message)

    if cipher_direction in {'decode', 'dec', 'd', 'descodificar', 'des'}:
        shift_amount *= -1

    if language in 'es':
        alphabet_len = len(alph_es)
    elif language in 'en':
        alphabet_len = len(alph_en)

    for char in split:
        if language in 'es':
            if char not in alph_es:
                rejoined.append(char)
                continue
            index = alph_es.index(char) + shift_amount
            if index >= alphabet_len:
                index -= alphabet_len
            elif index < 0:
                index += alphabet_len
            rejoined.append(alph_es[index])
        elif language in 'en':
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

    if cipher_direction in {'encode', 'enc', 'e', 'codificar', 'cod', 'c'}:
        if language in 'es':
            return f'\nEl texto codificado es: {cipher_text.capitalize()}\n'
        elif language in 'en':
            return f'\nThe encoded text is: {cipher_text.capitalize()}\n'

    elif cipher_direction in {'decode', 'dec', 'd', 'descodificar', 'des'}:
        if language in 'es':
            return f'\nEl texto descodificado es: {cipher_text.capitalize()}\n'
        elif language in 'en':
            return f'\nThe decoded text is: {cipher_text.capitalize()}\n'


def restart(language: str):
    """
    Restart the game.
    """
    if language in 'es':
        choice = input('¿Quieres volver a encriptar o desencriptar un mensaje? Teclea "Sí" o "No": ').lower()
        if choice in ('si', 'sí', 's'):
            clear()
            program_es(language)
        else:
            print('\n¡Adiós!')
            quit()
    elif language in 'en':
        choice = input('Do you want to go again? Type "Yes" or "No": ').lower()
        if choice in ('yes', 'y'):
            clear()
            program_en(language)
        else:
            print('\nGoodbye')
            quit()


def program_es(language: str):
    """
    Spanish version of the main program.
    """
    direction = text_direction(language)
    text = input("\nIntroduce el mensaje: ").lower()
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

    print(caesar(language, text, shift, direction))

    restart(language)


def program_en(language: str):
    """
    English version of the main program.
    """
    direction = text_direction(language)
    text = input("\nType your message: ").lower()
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

    print(caesar(language, text, shift, direction))

    restart(language)


def main():
    """
    Main function. Checks user language and calls the correct version of the game.
    """
    lang = language_matching(get_lang())

    if lang in 'es':
        program_es(lang)
    elif lang in 'en':
        program_en(lang)


main()
