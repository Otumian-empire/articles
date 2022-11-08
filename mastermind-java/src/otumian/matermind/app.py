# Import the _random_ module
import random

# The number of times to play must be even between 2 to 12 rounds
while True:
    try:
        rounds = int(input("Enter number of rounds (Even in [2, 12]): "))

        if rounds >= 2 and rounds <= 12 and rounds % 2 == 0:
            break

    except ValueError:
        print("Round must be an even number from 2 to 12 includes")


# should there be duplicates
try:
    duplicates_allowed = int(input("Duplicates allowed? (1/0) "))
except ValueError:
    duplicates_allowed = 0


# The number of codes we will be dealing with will four
NUMBER_CODE = 4


# The code maker
code_maker = []
counter = 0

while counter < NUMBER_CODE:
    code = random.randint(0, 9)

    if duplicates_allowed:
        code_maker.append(code)
        counter += 1

    else:
        if not code in code_maker:
            code_maker.append(code)
            counter += 1


# hint
hints = ['h', 'i', 'n', 't']


# code breaker guesses the code by the code maker
while rounds > 0:

    # enter guess with spaces
    code_breaker = list(map(int, input("Enter codes space separated: ").split()))

    # compare the code_breaker to the code maker
    for i in range(NUMBER_CODE):
        if code_breaker[i] > code_maker[i]:
            hints[i] = 1
        elif code_breaker[i] == code_maker[i]:
            hints[i] = 0
        else:
            hints[i] = -1

    # because of the values that we used to hint the user
    # we have to find some dicey way to break the program
    # when the user guess the code
    if hints.count(0) == 4:
        break

    print(hints)

    rounds -= 1


# declaring the result of the game
if rounds > 0:
    print("You won the rounds")
else:
    print("You lost bitterly to a computer")

print(code_maker)

