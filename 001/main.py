"""
    Day 01 - Project: Band Name Generator

    coded by JcSilverX
"""

print('Welcome to the Band Name Generator.')
city = str(input('What`s name of the city you grew up in?\n'))
pet = str(input('What`s your pet`s name?\n'))

name = ' '.join([city, pet])

print(f'Your band name could be {name}.\n')
