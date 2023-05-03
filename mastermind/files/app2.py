# app2.py

# Import the _random_ module
import random
import os
from time import sleep


# string constants
ROUNDS_PROMPT = "Enter number of rounds (Even in [2, 12]) 🤗️: "
INVALID_ROUNDS_PROMPT = "Round must be an even number from 2 to 12 includes 😩️"
DUPLICATE_PROMPT = "Duplicates allowed? (1/0) 🤤️: "
CODE_BREAKER_PROMPT = "Enter codes separated by space: "
WIN_PROMPT = "You won the rounds 👏️"
LOSS_PROMPT = "You lost bitterly to a computer 😏️"

# int constants
ZERO, ONE = 0, 1
NUMBER_CODE = 4
TERMINATING_VALUE = 0
MORE, EQUAL, LESS = 1, 0, -1
MIN_ROUNDS, MAX_ROUNDS = 2, 12
RAND_INT_MIN, RAND_INT_MAX = 0, 9
WAITING_TIME = 3

# The code maker
code_maker = []

# hint
hints = ['h', 'i', 'n', 't']

def clear_screen() :
    os.system('cls' if os.name == 'nt' else 'clear')

# validates the round input
def isvalid_round(rounds):
    return MIN_ROUNDS <= rounds <= MAX_ROUNDS and rounds % 2 == ZERO

# declaring the result of the game
def declare_result(rounds):
    if rounds > TERMINATING_VALUE:
        print(WIN_PROMPT)
    else:
        print(LOSS_PROMPT)

# generate code maker
def generate_code_maker(duplicates_allowed):
    counter = 0

    while counter < NUMBER_CODE:
        code = random.randint(RAND_INT_MIN, RAND_INT_MAX)

        if duplicates_allowed:
            code_maker.append(code)
            counter += ONE
        else:
            if not code in code_maker:
                code_maker.append(code)
                counter += ONE

# compare the code_breaker to the code maker
def compare_code():
    # enter guess with spaces
    code_breaker = list(map(int, input(CODE_BREAKER_PROMPT).split()))

    for pos in range(NUMBER_CODE):
        if code_breaker[pos] > code_maker[pos]:
            hints[pos] = MORE
        elif code_breaker[pos] == code_maker[pos]:
            hints[pos] = EQUAL
        else:
            hints[pos] = LESS
            
# entry point
def App():
    # The number of times to play must be even between 2 to 12 rounds
    while True:
        try:
            rounds = int(input(ROUNDS_PROMPT))

            if isvalid_round(rounds):
                break

        except ValueError:
            print(INVALID_ROUNDS_PROMPT)

    # should there be duplicates
    try:
        duplicates_allowed = int(input(DUPLICATE_PROMPT))
    except ValueError:
        duplicates_allowed = ZERO

    generate_code_maker(duplicates_allowed)

    # code breaker guesses the code by the code maker
    while rounds > TERMINATING_VALUE:
        compare_code()

        # because of the values that we used to hint the user
        # we have to find some dicey way to break the program
        # when the user guess the code
        if hints.count(EQUAL) == NUMBER_CODE:
            break

        print(hints)

        rounds -= ONE

    declare_result(rounds)

    print(code_maker)

# infinitely keep playing
while True:
    App()

    sleep(WAITING_TIME)
    clear_screen()

    # reset the game for replay
    code_maker = []
    hints = ['h', 'i', 'n', 't']
