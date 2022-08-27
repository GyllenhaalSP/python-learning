"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
import pandas as pd
from unidecode import unidecode

nato_dict = {data.letter: data.code for index, data in pd.read_csv('nato_phonetic_alphabet.csv').iterrows()}

while word := input('What word do you want to convert?: '):
    try:
        if word in {'e', 'end', 's', 'stop', 'q', 'quit'}:
            break
        print([nato_dict[char] for char in unidecode(word).upper()], end='\n\n')
    except KeyError:
        print('Sorry, only letters in the alphabet, please!\n')

print('\nBye')
