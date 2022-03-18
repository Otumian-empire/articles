from http.client import HTTPSConnection as httpConn
from string import (
    ascii_letters, ascii_lowercase, ascii_uppercase,
    digits, punctuation, whitespace)


class Validator:
    def is_email_valid(self, email=""):
        """ returns a bool if a an email, is a valid one with the domain as a tuple"""

        # according to the link, these emails are valid but they fail here
        # ref on
        # email: https://stackoverflow.com/questions/2049502/what-characters-are-allowed-in-an-email-address

        # emails = [
        #     '"very.unusual.@.unusual.com"@example.com',
        #     '"very.(),:;<>[]\".VERY.\"very@\ \"very\".unusual"@strange.example.com',
        #     "#!$%&'*+-/=?^_`{}|~@example.org",
        #     '"()<>[]:,;@"!#$%&\'-/=?^_`{}| ~.a"@example.org'
        # ]

        # certain punctuations aren't allowed in an email except in a quote
        # except, space -  ' ' in a quoted local, the rest are unacceptable
        # learnt that + can be used in XSS so we'd remove it
        valid_chars = {'-', '_', '.'}
        invalid_chars = set(punctuation + whitespace) - valid_chars

        # check if email is set, it is not an empty string
        if not email:
            return False

        # strip leading and ending spaces
        email = email.strip()

        at_char = "@"
        dot = "."
        hyphen = "-"
        dbl_quote = '"'

        # thus email must have @
        if at_char not in email:
            return False

        # there must be one and only one @
        if email.count(at_char) > 1:
            return False

        # split the email into local and domain part
        local, domain = email.split(at_char)

        # check for invalid characters in quote
        # any other char except, _ - ., should be in double quote
        # spaces are allowed inside the local without a quote
        for char in invalid_chars:
            if (
                char in local
                and (not local.startswith(dbl_quote)
                     or not local.endswith(dbl_quote))):
                return False

        # quote string must be dot seperated or a dot shouldn't follow a dot
        if dot in local:
            try:
                dot_position_in_local = local.index(dot)

                if local[dot_position_in_local + 1] == dot:
                    return False
            except:
                print("There is no dot in the local")
                return False

        # local.startswith('.') and local.endswith('.') == False
        if local.startswith(dot) or local.endswith(dot):
            return False

        # domain, - can't be first or last char
        if domain.startswith(hyphen) or domain.endswith(hyphen):
            return False

        # quote string must be dot seperated or a dot shouldn't follow a dot
        # in domain
        dot_position_in_domain = domain.index(dot)
        if dot in domain and (domain[dot_position_in_domain] == domain[dot_position_in_domain + 1]):
            return False

        # domain, . cant't be first or last char
        if domain.startswith(dot) or domain.endswith(dot):
            return False

        return True

    def email_exist(self, domain):
        """ ping the domain's server to see if the domain actual exists
        using http.client and get a responds of 200 OK """

        conn = httpConn(domain)
        conn.request("HEAD", "/")
        res = conn.getresponse()

        if res.status != 200 or res.reason != "OK":
            return False
        return True
