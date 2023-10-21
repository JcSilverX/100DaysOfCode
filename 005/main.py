"""
    Day 05 - Project: PyPassword Generator

    coded by JcSilverX
"""

import random # choice


LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' 'z']
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pyPassword(length):
    password = LETTERS + DIGITS + SYMBOLS
    return ''.join(random.choice(password) for k in range(length))


def validate_input(inp):
    try:
        input_value = int(inp)
        if input_value < 4:
            err_exit('Invalid input.')
        return input_value
    except ValueError as err:
        err_exit(err)


def err_exit(error):
    print(error)
    exit()


if __name__ == '__main__':
	print('Welcome to the PyPassword Generator!')
	nchars = validate_input(input('How many characters would you like in your password? '))
    
	generated_password = pyPassword(nchars)
	print(generated_password)