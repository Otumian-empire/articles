from string import ascii_letters


def get_schar_count(data='', sack=[]):
    """
    Returns the number of specific characters in data that is in sack
    By default, data is an empty string and sack is an empty list
    Both data and list, are iterables
    If neither data or sack is set, zero in returned
    """

    if not data or not sack:
        return 0

    counter = 0

    for char in data:
        if char in sack:
            counter += 1

    return counter


sack = [c for c in ascii_letters]

print(sack)
data = "password"
print(get_schar_count(data, sack))
