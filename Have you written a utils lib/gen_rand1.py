from string import ascii_letters, digits
from random import randint

def generate_token():
    TOKEN_LENGTH = 6
    token = ""

    code_alphabet = ascii_letters + digits + "_"

    max = len(code_alphabet)

    for i in range(TOKEN_LENGTH):
        token += code_alphabet[randint(0, max - 1)]

    return token


for i in range(5):
    print(generate_token())