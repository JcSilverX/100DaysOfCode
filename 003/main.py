"""
    Day 03 - Project: Treasure Island

    coded by JcSilverX
"""

FILE_NAME = 'ASCII-art.txt'

try:
    with open(FILE_NAME) as f:
        print(f.read())
except FileNotFoundError:
    print(f'file: {FILE_NAME} was not found.')
    exit()

print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

choice = str(input('You`re at a cross road. Where do you want to go? Type "left" or "right"\n')).lower()

if choice == 'left':
    choice = str(input('You`ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'))
    if choice == 'wait':
        choice = str(input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n'))
        if choice == 'yellow':
            print('You found the treasure! You Win!')
        elif choice == 'blue':
            print('You enter a room of beasts. Game Over.')
        else:
            print('You chose a door that doesn`t exist. Game Over.')
    else:
        print('You get attacked by an angry trout. Game Over.')
else:
    print('You fell into a hole. Game Over.')
