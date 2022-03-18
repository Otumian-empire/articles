from string import punctuation, whitespace


def is_email_valid(email=""):
    valid_chars = {'-', '_', '.'}
    invalid_chars = set(punctuation + whitespace) - valid_chars
    email = ""
    stripped_email = email.strip()

    # TODO: split the local and domain from the last @
    # email must have @
    if "@" not in stripped_email:
        return False

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
