"""
    Day 10 - Project: Calculator

    Coded by JcSilverX
"""

from art import LOGO
from opts import opts

"""
    calculator:
        - add
        - subtract
        - multiply
        - divide
"""
def calculator():
    flags = False
    
    n1 = validate_input(input('What`s the first number?: '))
    for symbol in opts:
        print(symbol)

    while not flags:
        opt_symbol = input('Pick an operation: ')
        n2 = validate_input(input('What`s the next number? '))

        func = opts[opt_symbol]
        ans = func(n1, n2)
        choice = input(f'Type `y` to continue calculating with {ans}, or type `n` to start a new calculation: ')
        if choice == 'n':
            flags = True
            calculator()
        elif choice == 'y':
            n1 = ans
        else:
            flags = True


def validate_input(inp):
    try:
        if '.' in inp:
            return float(inp)
        else:
            return int(inp)
    except ValueError as err:
        print(err)
        exit()

if __name__ == '__main__':
    print(f'{LOGO}')
    calculator()
