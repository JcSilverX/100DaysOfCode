"""
    Day 07 - Project: Hangman

    coded by JcSilverX
"""

import random

from hangman_art import LOGO, STAGES
from hangman_words import WORD_LIST



"""
    TODO 1 --
"""
def get_random_word():
    return random.choice(WORD_LIST)


"""
    TODO 2 --
"""
def guess_letter():
    guess = input('Guess a letter: ').lower()
    
    return guess


"""
    TODO 3 --
"""
def check(letter, list):
    return letter in list


"""
    TODO 4 --
"""
def init_list(chosen_word):
    return [ l.replace(l, '_') for l in str(chosen_word) ]


"""
    TODO 5 --
"""

# helper function
def find_indexes(guess, chosen_word):
    length = len(chosen_word)

    return [ index for index in range(length) if chosen_word.startswith(guess, index) ]


def update_list(guess, chosen_word, empty_l):
    indexes = find_indexes(guess, chosen_word)
    
    for index, _ in enumerate(empty_l):
        if index in indexes:
            empty_l[index] = guess
    return empty_l


"""
    TODO 6 --
"""
def display_list(list):
    print(' '.join(list))


if __name__ == '__main__':
    chosen_word = get_random_word()
    end_of_game = False
    lives = 6

    print(f'{LOGO}\n')

    empty_l = init_list(chosen_word)
    
    while not end_of_game:
        guess = guess_letter()

        if check(guess, empty_l):
            print(f'You`ve already guessed {guess}')

        guessed_letter = update_list(guess, chosen_word, empty_l)
        display_list(guessed_letter)


        if (check(guess, chosen_word)):
            continue
        else:
            lives -= 1
            print(f'You guessed {guess}, that`s not in the word. You lose a life.')
 
            print(STAGES[lives])
            if lives == 0:
                end_of_game = True
                print('You lose.')

        if not check('_', guessed_letter):
            end_of_game = True
            print('You win.')

    