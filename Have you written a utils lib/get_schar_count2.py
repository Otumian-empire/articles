def get_schar_count_loop(data):
    schar_count = {}

    for char in data:
        if char in schar_count:
            schar_count[char] += 1
        else:
            schar_count[char] = 1

    return schar_count


def get_schar_count_dict(data):
    schar_count = {}

    for char in data:
        char_count = schar_count.get(char, 0)
        schar_count[char] = char_count + 1

    return schar_count


def get_schar_count(data):
    schar_count = {}

    for char in data:
        if char not in schar_count:
            schar_count[char] = 0

        schar_count[char] += 1

    return schar_count


def get_schar_count3(data):
    schar_count = {}

    for char in data:
        schar_count.setdefault(char, 0)
        schar_count[char] += 1

    return schar_count


def get_schar_count_comp(data):
    return {char: data.count(char) for char in set(data)}


# print(get_schar_count_loop("he+llo"))
# print(get_schar_count_dict("hello"))
# print(get_schar_count("hello"))
print(get_schar_count3("hello"))
