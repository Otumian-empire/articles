from datetime import datetime
from http.client import HTTPSConnection as httpConn
from passlib.hash import bcrypt
from random import randint
from string import (
    ascii_letters, ascii_lowercase, ascii_uppercase,
    digits, punctuation, whitespace)


class Generator:
    """ Return generated values """

    # this token is for the change of email and password
    def generate_token(self):
        """ returns a random alphanumeric characters, given the length of the data desired.
        this random token generator def is provided by Scott.
        source: https:stackoverflow.com/a/137335884592338 """

        TOKEN_LENGTH = 6

        token = ""

        code_alphabet = ascii_letters + digits + "_"

        max = len(code_alphabet)

        for i in range(TOKEN_LENGTH):
            token += code_alphabet[randint(0, max - 1)]

        return token

    def get_schar_count(self, data='', sack=[]):
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

    def get_bcrypt_hashed_passwd(self, password):
        """ hash the password using bcrypt from passlib.hash """
        # use bcrypt to hash the password
        return bcrypt.hash(password)

    def get_current_date_time(self):
        # get the current date and time
        now = datetime.now()

        # format the datetime using
        # [month, day, year, hour, minute, sec]
        # [%B, %d, %Y, %H, %M, %S] : December 2, 1996 - 13:24:20
        # return now.strftime("A%, %d %B, %Y - %H:%M:%S")
        return now.strftime("%B %d, %Y - %H:%M:%S")


class DataSizeRange:
    """
    Set the min_range and max_range for data to evalute valid size
    By default, min_range=6 and max_range=20
    """

    def __init__(self, min_range=6, max_range=20):
        self.min_range = min_range
        self.max_range = max_range


class Validator:

    def validate_size(self, data, dataSizeRange):
        """
        Pass DataSizeRange Object to the validate_size method with the required range
        Returns True if size (len) of data is in bounded inclusively else, False
        """
        return dataSizeRange.min_range <= len(data) <= dataSizeRange.max_range

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

    def is_valid_password(self, password):
        """ returns True when the password  is valid, else False.
        The password must satisfy these conditions:
        * no leading or trailing white spaces - so we strip them off
        * Should be between 6 to 20 characters long
        * must exclude any of these, {*%;<>\{}[]+=?&,:'"` } and blank space
        * must have at least one number.
        * must have at least one lowercase character.
        * must have at least one uppercase character.
        * must have at least one special symbol. {!@#$^&()_.-}.
        """

        # Conditions for a valid password are:

        # password must not be a falsy, empty str or 0 or white space
        if not password:
            return False

        # no leading or trailing while spaces spaces
        password = password.strip()

        # Should be between 6 to 20 characters long. there is the notion
        # of no max limit. I think the size function should handle this
        MIN_PASS_SIZE = 6
        MAX_PASS_SIZE = 20

        if not Validator().validate_size(
                password, DataSizeRange(MIN_PASS_SIZE, MAX_PASS_SIZE)):
            return False

        # avoid {*%;<>\{}[]+=?&,:'"` } and blank space
        valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
        invalid_chars = set(punctuation + whitespace) - valid_chars

        for char in invalid_chars:
            if char in password:
                return False

        # Should have at least one number.
        if Generator().get_schar_count(password, digits) < 1:
            return False

        # Should have at least one uppercase and one lowercase character.
        if Generator().get_schar_count(password, ascii_uppercase) < 1:
            return False

        if Generator().get_schar_count(password, ascii_lowercase) < 1:
            return False

        # Should have at least one special symbol. {!@#$^&()_.-}.
        if Generator().get_schar_count(password, valid_chars) < 1:
            return False

        return True

    def is_valid_hash(self, password, hashed_password):
        return bcrypt.verify(password, hashed_password)
