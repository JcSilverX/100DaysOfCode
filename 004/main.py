"""
    Day 04 - Project: Rock Paper Scissors

    src: https://wrpsa.com/the-official-rules-of-rock-paper-scissors/
    

    coded by JcSilverX
"""

import random # randint

ROCK =  \
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = \
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = \
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [ROCK, PAPER, SCISSORS]

# possible winning combinations.
WINNING_COMBINATIONS = [
    [0, 2],
    [1, 0],
    [2, 1]
]


def get_choice(choice):
    return choice, choices[choice]


def isDraw(your_choice, computer_choice):
    return your_choice == computer_choice


def isWinner(your_choice, computer_choice):
    for w in WINNING_COMBINATIONS:
        if [your_choice, computer_choice] == w:
            return True
    return False


def validate_input(inp):
    
    try:
        input_value = int(inp)
        if input_value >= 0 and input_value < 3:
            return input_value
        else:
            err_exit('''\
                An error has occurred.

                HINT:
                    Please select a whole number that falls between 0 and 2.
            ''')
    except ValueError as err:
        err_exit(err)


def err_exit(error):
    print(error)
    exit()


if __name__ == '__main__':
    choice_one, your_choice = get_choice(validate_input(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')))
    choice_two, computer_choice = get_choice(validate_input(random.randint(0, 2)))

    print(f'your_choice: {your_choice}\ncomputer_choice: {computer_choice}')

    if isDraw(your_choice, computer_choice):
        print('is a draw')

    elif isWinner(choice_one, choice_two):
        print('You win')
    else:
        print('You lose.')
