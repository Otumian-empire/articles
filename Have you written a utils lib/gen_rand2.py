from string import ascii_letters, digits
from random import randint


def generate_token(token_size=6):
    token_source = ascii_letters + digits + "_"

    start_point = 0
    end_point = len(token_source) - 1

    return "".join(
        token_source[randint(start_point, end_point)]
        for _ in range(token_size)
    )


for i in range(5):
    print(generate_token(i + 4))
