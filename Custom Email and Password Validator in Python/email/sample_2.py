# sample_2.py

from audioop import reverse
from string import punctuation, whitespace


# add type annotations
def is_email_valid(email: str) -> bool:
    # email must be of type string
    if type(email) != str:
        return False

    # make the valid characters a constant to be used through out the code
    HYPHEN_CHAR = "-"
    UNDERSCORE_CHAR = "_"
    DOT_CHAR = "."
    AT_CHAR = "@"

    valid_chars = {HYPHEN_CHAR, UNDERSCORE_CHAR, DOT_CHAR}
    invalid_chars = set(punctuation + whitespace) - valid_chars

    stripped_email = email.strip()

    # email must have @. this @ must separate the local and domian
    # there might be an email with several @ so we'd need the last @.
    # we could check if @ in in email and split the email to check
    # if there are at least two @ characters. We will pick the local
    # and domain from the last
    if AT_CHAR not in stripped_email:
        return False

    at_splitted_email = stripped_email.split(AT_CHAR)
    size_at_splitted_email = len(at_splitted_email)
    local = "".join(at_splitted_email[:size_at_splitted_email-1])
    domain = "".join(at_splitted_email[-1])

    # An email can have several "@" characters but one must separate the local
    # from the domain and the rest must be part of the local, all in quotes
    # It could be "@user@name@"@gmail.com or "@".user."@".name@"@gmail.com

    # there must be one @
    if stripped_email.count("@") != 1:
        return False

    # split the email into local and domain part
    local, domain = stripped_email.split("@")

    for char in invalid_chars:
        if (
            char in local
            and (not local.startswith('"')
                 or not local.endswith('"'))):
            return False

    if "." in local:
        try:
            dot_position_in_local = local.index(".")

            if local[dot_position_in_local + 1] == ".":
                return False
        except:
            return False

    # local.startswith('.') and local.endswith('.') == False
    if local.startswith(".") or local.endswith("."):
        return False

    # domain, - can't be first or last char
    if domain.startswith("-") or domain.endswith("-"):
        return False

    # domain, . cant't be first or last char
    if domain.startswith(".") or domain.endswith("."):
        return False

    # dots in email must not be sequential
    dot_position_in_domain = domain.index(".")

    if "." in domain and (domain[dot_position_in_domain] == domain[dot_position_in_domain + 1]):
        return False

    return True


s = "hello"
t = s[::-1]

print(s)
print(t)
