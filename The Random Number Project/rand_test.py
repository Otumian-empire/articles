import sys
from random import randint


# constants for each test (options)
MEAN_TEST = 1
FREQUENCY_TEST = 2
SERIAL_TEST = 3
POKER_TEST = 4
POKER_TEST_FILE = 5

# constant for reading and writing to file
# filename - poker.txt
POKER_TEST_FILENAME = "poker.txt"
WRITE_MODE = "w"
READ_MODE = "r"

# argument count - user must pass a test option
# which indicates which test to run this increases
# argc to 2 (including the program filename)
ARGUMENT_COUNT = 2


# prompt user to enter an option (number) indicating a test
# to run when no option is passed when running the program
def promptUser():
    print("Pass 1, 2, 3 or 4 to run Mean, Frequency, ", end="")
    print("Serial or Poker Test respectively.")


# returns a random number
def genRand():
    return randint(0, 9)


# compare all 4 digits to be equal
# (return 1 for True and 0 for False)
def hasFourDigitsEqual(a, b, c, d):
    return a == b and b == c and c == d


# compare all 4 digits, for 3 equal digits to be equal
# (return 1 for True and 0 for False)
def hasThreeDigitsEqual(a, b, c, d):
    if (a == b and b == c):
        return True
    elif (a == b and b == d):
        return True
    elif (a == c and c == d):
        return True
    elif (b == c and c == d):
        return True

    return False


# compare all 4 digits, for 2 pairs repeated
# (return 1 for True and 0 for False)
# NB: 2222 will pass but will fail in this case
# because of the arrangement of the if and else statements
def hasTwoPairDigitsEqual(a, b, c, d):

    if (a == b and c == d):
        return True
    elif (a == c and b == d):
        return True
    elif (a == d and b == c):
        return True

    return False


# compare all 4 digits, for 1 pair repeated
# (return 1 for True and 0 for False)
def hasOnePairDigitsEqual(a, b, c, d):
    if (a == b):
        return True
    elif (a == c):
        return True
    elif (a == d):
        return True
    elif (b == c):
        return True
    elif (b == d):
        return True
    elif (c == d):
        return True

    return False


# prints the mean of 1000 trials
def meanTest():

    rounds = 1000
    mean = 0

    for _ in range(rounds):
        mean += genRand()

    mean /= rounds

    print("Mean Test of %i", rounds)
    print("Mean = %.1f", mean)


# prints a table percentages for 10000 trials for value [0, 9]
def frequencyTest():
    rounds = 10000
    range_ = 10
    totalPercentage = 100.0
    frequency = [0]*range_

    for _ in range(rounds):
        frequency[genRand()] += 1

    print(f"Frequency Test of {rounds}")

    print(f"X  |  % ")
    print("--------")

    for i in range(range_):
        print(f"{i}  |  {float(frequency[i] / totalPercentage)} ")


# prints a table percentages for 10000 trials for
# pairs of values [00, 99]
def serialTest():
    rounds = 10000
    range_ = 10
    totalPercentage = 100.0
    frequency = [[0]*range_ for i in range(range_)]

    for i in range(rounds):
        frequency[genRand()][genRand()] += 1

    print(f"Serial Test of {rounds}")

    print(" X  Y  |  % ")
    print("--------------")

    for i in range(range_):
        for j in range(range_):
            print(f" {i}  {j}  |  {float(frequency[i][j] / totalPercentage)} ")


# prints tables of 4-digit values of different classes
# classes:
#     all_the_same -> all 4 digits are the same (repeated 4)
#     three_the_same -> 3 of 4 are the same (repeated 3)
#     two_pair -> 2 pairs of 4 are the same (2, 2 repeated)
#     one_pair -> 2 of 4 are the same (1, 2 repeated)
#     none_identical -> all 4 are different (no repeat)
def pokerTest():
    rounds = 1000

    # if same class, add to same class
    # elif trio class, add to trio class
    # elif duo class, add to duo class
    # elif mono class, add to mono class
    # else add to unique class
    all_the_same = 0
    three_the_same = 0
    two_pair = 0
    one_pair = 0
    none_identical = 0

    # generate 4 randon numbers, 1000 times (hold 1000 trials)
    for i in range(rounds):
        # get the random numbers to compair them
        digit_1 = genRand()
        digit_2 = genRand()
        digit_3 = genRand()
        digit_4 = genRand()

        if (hasFourDigitsEqual(digit_1, digit_2, digit_3, digit_4)):
            all_the_same += 1
        elif (hasThreeDigitsEqual(digit_1, digit_2, digit_3, digit_4)):
            three_the_same += 1
        elif (hasTwoPairDigitsEqual(digit_1, digit_2, digit_3, digit_4)):
            two_pair += 1
        elif (hasOnePairDigitsEqual(digit_1, digit_2, digit_3, digit_4)):
            one_pair += 1
        else:
            none_identical += 1

    print(f"Poker Test of {rounds}")

    print("number of digits    | %")
    print("-------------------------")
    print(f"all the same        | {all_the_same}")
    print(f"3 digits the same   | {three_the_same}")
    print(f"two pairs           | {two_pair}")
    print(f"one pairs           | {one_pair}")
    print(f"none identical      | {none_identical}")


# poker test - reading digits from file
def pokerTestFile():
    rounds = 4000

    # file pointer
    # Write 4000 random numbers into POKER_TEST_FILENAME
    with open(POKER_TEST_FILENAME, WRITE_MODE) as fp:
        for i in range(rounds):
            print(f"{genRand()} ", end="", file=fp)

    # open file for reading and read the file content
    with open(POKER_TEST_FILENAME, READ_MODE) as fp:
        all_the_same = 0
        three_the_same = 0
        two_pair = 0
        one_pair = 0
        none_identical = 0

        content = fp.read().strip(" ").split(" ")

        for i in range(0, len(content), 4):
            fourSet = [
                int(digit) for digit in content[i: i+4]
            ]

            digit_1, digit_2, digit_3, digit_4 = fourSet

            if hasFourDigitsEqual(digit_1, digit_2, digit_3, digit_4):
                all_the_same += 1
            elif hasThreeDigitsEqual(digit_1, digit_2, digit_3, digit_4):
                three_the_same += 1
            elif hasTwoPairDigitsEqual(digit_1, digit_2, digit_3, digit_4):
                two_pair += 1
            elif hasOnePairDigitsEqual(digit_1, digit_2, digit_3, digit_4):
                one_pair += 1
            else:
                none_identical += 1

    print(f"Poker Test of {4 * rounds} random numbers from file")
    print("number of digits   |  % ")
    print("------------------------")
    print(f"all the same       | {all_the_same/100}")
    print(f"3 digits the same  | {three_the_same/100}")
    print(f"two pairs          | {two_pair/100}")
    print(f"one pairs          | {one_pair/100}")
    print(f"none identical     | {none_identical/100}")


if __name__ == "__main__":
    try:
        argc = len(sys.argv)

        if argc != ARGUMENT_COUNT:
            promptUser()
        else:
            # get the test option passed by the user from argv[1]
            testOption = int(sys.argv[1])

            if (testOption == MEAN_TEST):
                meanTest()

            elif testOption == FREQUENCY_TEST:
                frequencyTest()

            elif testOption == SERIAL_TEST:
                serialTest()

            elif testOption == POKER_TEST:
                pokerTest()

            elif testOption == POKER_TEST_FILE:
                pokerTestFile()

            else:
                print("Test Not Known")
                promptUser()
    except:
        promptUser()
