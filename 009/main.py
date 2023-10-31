"""
    Day 09 - Project: Secret Auction Program Instructions and Flow Chart

    Coded by JcSilverX
"""
from art import LOGO
import os

if __name__ == '__main__':
    flag = False
    d = dict()

    print(f'{LOGO}')
    print('Welcome to the secret auction program.')

    while not flag:
        name = str(input('What is your name? '))
        bid = int(input('Wha`s your bid? $'))
        d[name] = bid

        choice = str(input('Are there any other bidders? Type `yes` or `no`: '))
        if choice == 'no':
            bidder = max(d, key=lambda key: d[key])
            os.system('clear')
            print(f'The winner is {bidder} with a bid of ${d[bidder]}.')
            flag = True
        else:
            os.system('clear')

