"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
import time

start = time.perf_counter()

with open('./Input/Letters/starting_letter.txt') as letter:
    with open('./Input/Names/invited_names.txt') as invited:
        individual_names = [name.replace("\n", "") for name in invited]
        full_letter = letter.read()
        for name in individual_names:
            new_letter = full_letter.replace('[name]', name)
            with open(f'./Output/letter_to_{name}.txt', 'w') as saved_file:
                saved_file.write(new_letter)
end = time.perf_counter()

print(f'Automatic letter writing completed in {end - start:.05f} seconds.')
