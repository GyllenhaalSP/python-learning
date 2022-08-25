"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
import pandas as pd

nato_dict = {data.letter: data.code for index, data in pd.read_csv('nato_phonetic_alphabet.csv').iterrows()}

while word := input('What word do you want to convert? (empty field to exit): '):

    print([nato_dict[char] for char in word.upper() if char in nato_dict], end='\n\n')

print('\nBye')
