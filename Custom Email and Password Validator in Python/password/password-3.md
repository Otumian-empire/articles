# Custom Password Validation in Python (Unit test the function for password validation)

These posts will be in three parts.

1. Function for password validation
2. Refactoring the function for password validation
3. Unit test the function for password validation

This is the third and final part of the Custom Password Validation in Python series. We will look at **Unit test the function for password validation**.

{% post https://dev.to/otumianempire/custom-password-validation-in-python-refactoring-the-function-for-password-validation-2i95 %}

Below is the code we had after the refactor:

```python
from string import (
    ascii_lowercase, ascii_uppercase,
    digits, punctuation, whitespace)


def contains_character(password: str = "", sack: str = "") -> bool:
    has_char = False

    for char in password:
        if char in sack:
            has_char = True
            break

    return has_char


def is_valid_size(password: str = "") -> bool:
    MIN_SIZE = 6
    MAX_SIZE = 20
    password_size = len(password)

    return MIN_SIZE <= password_size <= MAX_SIZE


def get_invalid_chars():
    valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
    invalid_chars = set(punctuation + whitespace) - valid_chars

    return "".join(invalid_chars)


def is_valid_password(password: str = "") -> bool:
    try:
        if not password:
            return False

        new_password = password.strip()

        if not is_valid_size(new_password):
            return False

        invalid_chars = get_invalid_chars()

        if contains_character(new_password, invalid_chars):
            return False

        if not contains_character(new_password, digits):
            return False

        if not contains_character(new_password, ascii_lowercase):
            return False

        if not contains_character(new_password, ascii_uppercase):
            return False

        return True
    except:
        return False
```

Our aim here is to write unit tests for the snippet above. We can catch hidden bugs and continue with the refactoring as we fix the code to pass the tests.

## Before Test 🔩️

Somethings you should know:

-   This will be a unit test
-   We would make use of python's built-in test module, `unittest`
-   We will test, `contains_character`, `is_valid_size` and `is_valid_password` in order
-   Tests will be in `test.py` so the snippet above could be in `app.py` (you choose the name you want)
-   We will refer to {% post https://dev.to/otumianempire/python3-programming-exercise-22-1b1j %}.

## Test `contains_character`

`contains_character` returns a `bool`, either `True` or `False`. So we can use the `assertTrue` and the `assertFalse` methods.

We will test:

-   if neither password nor sack is passed (No argument)
-   for the character `"i"` in the string, `"python"`
-   for the character `"py"` in the string, `"python"`
-   for the character `"python"` in the string, `"python"`

There are cases like when an `int` is passed as `password` or when a `list` is passed as `sack`. We won't be testing for such cases. (You should test for that)

### TestContainsCharacter

```python
import unittest
from app import contains_character


class TestContainsCharacter(unittest.TestCase):
    def test_empty_password_or_and_empty_sack(self):
        self.assertFalse(contains_character())

    def test_char_i_in_str_python(self):
        self.assertFalse(contains_character("i", "python"))

    def test_str_py_in_str_python(self):
        self.assertTrue(contains_character("py", "python"))

    def test_str_python_in_str_python(self):
        self.assertTrue(contains_character("python", "python"))

if __name__ == "__main__":
    unittest.main()
```

We can hit `ctrl + F5` run this script (`test.py`) without debugging. We can run this script as `python3 test.py` or `python3 -m unittest test.py`. All these tests should pass.

## Test `is_valid_size`

`is_valid_size` returns a `bool`, either `True` or `False`. So we can use the `assertTrue` and the `assertFalse` methods.

We will test:

-   for an empty password or when no argument is passed
-   for four characters password
-   for six characters password
-   for sixteen characters password
-   for twenty characters password
-   for twenty-one characters password

### TestIsValidSize

```python
import unittest
from app import is_valid_size


class TestIsValidSize(unittest.TestCase):
    def test_empty_password(self):
        self.assertFalse(is_valid_size(""))

    def test_4_char_password(self):
        self.assertFalse(is_valid_size("pass"))

    def test_6_char_password(self):
        self.assertTrue(is_valid_size("passwd"))

    def test_16_char_password(self):
        self.assertTrue(is_valid_size("ThisIs1Password!"))

    def test_20_char_password(self):
        self.assertTrue(is_valid_size("ThisIs1Password!+20"))

    def test_21_char_password(self):
        self.assertFalse(is_valid_size("ThisIs1Password!+20&"))


if __name__ == "__main__":
    unittest.main()
```

All these tests should pass.

## Test `is_valid_password`

`is_valid_password` returns a `bool`, either `True` or `False`. So we can use the `assertTrue` and the `assertFalse` methods.

We will test:

-   for an empty password
-   for three characters password
-   for ten characters password
-   for twenty characters password
-   for password with an invalid special character like a semicolon
-   for a password without a digit
-   for a password without a lower case
-   for a password without an upper case
-   for a password without a valid special character
-   for a valid password with
    -   a size within, _[6-20]_
    -   at least a lower and upper case character
    -   at least a digit
    -   no invalid special character

### TestIsValidPassword

```python

class TestIsValidPassword(unittest.TestCase):
    def test_empty_password(self):
        self.assertFalse(is_valid_password())

    def test_password_of_size_three(self):
        self.assertFalse(is_valid_password("pas"))

    def test_password_of_size_ten(self):
        self.assertFalse(is_valid_password("Password12"))
        self.assertTrue(is_valid_password("Password1_"))

    def test_password_of_size_twenty(self):
        self.assertFalse(is_valid_password("Password12Password_$"))

    def test_password_with_invalid_special_character_semicolon(self):
        self.assertFalse(is_valid_password("Password1_;"))
        self.assertFalse(is_valid_password("Password1;"))

    def test_password_with_no_digit(self):
        self.assertFalse(is_valid_password("Password_"))

    def test_password_with_no_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD1_"))

    def test_password_with_no_uppercase(self):
        self.assertFalse(is_valid_password("password1_"))

    def test_password_without_valid_special_character(self):
        self.assertFalse(is_valid_password("Password1"))

    def test_valid_password(self):
        self.assertTrue(is_valid_password("Password1_"))
        self.assertTrue(is_valid_password("PassWord34$"))


if __name__ == "__main__":
    unittest.main()
```

Well, not all the tests passed. These test cases shouldn't pass - we expect them not to pass. So when we expect `False` we get `True`. There is a flaw or bug somewhere.

These tests were those that were not passing:

-   `test_password_of_size_ten`: `self.assertFalse(is_valid_password("Password12"))` should be `False` because it has no special character even though the size is valid.
-   `test_password_without_valid_special_character`: `self.assertFalse(is_valid_password("Password1"))` should be `False` since there is no valid special character.

> The `is_valid_password` function doesn't check for the presence of a valid special character. It does check for invalid characters but not for valid characters. This was caused by the flawed assumption that, as far as the password doesn't contain invalid characters, then it contains valid characters (including valid special characters).

### Refactor `is_valid_password`

Now that we have pointed out the bug we had, we should make changes and rerun the tests.

Changes to make:

-   In `get_invalid_chars`, we have a `set` of valid special characters, `valid_chars`. Let's make it global to all the functions (i.e take it out of the `get_invalid_chars` function and put it at the top of the functions). To make sure nothing is broken somewhere, run the test (we expect two cases to fail). Note here that, even though we move `valid_chars` out of `get_invalid_chars`, `get_invalid_chars` should still function normally.

-   The `valid_chars` is a `set`, it can be used as a set in `get_invalid_chars`. `contains_character` takes a `string` `sack` as argument. We have to parse `valid_chars` as `string`. Let's create a function below `get_invalid_chars` to return a `string` version of `valid_chars`

    ```python
    def get_valid_chars():
        return "".join(valid_chars)
    ```

    Run the tests.

-   Let's check for valid characters in `is_valid_password` by adding the snippet below, before the `return True` statement in the `try` block.

    ```python
    if not contains_character(new_password, get_valid_chars()):
        return False
    ```

    Run the tests. Now, all the tests pass. Hurray!! 👏️👏️👏️

-   This is more of rearranging the code in `is_valid_password` in a certain other that works well naturally. We will reorder the code in `is_valid_password` in this order respectively: `size, lower case, upper case, digit, invalid special character and valid special character` Run the tests.

## Conclusion

The `is_valid_password` will be in `app.py` and would look like the snippet below:

```python
from string import (ascii_lowercase, ascii_uppercase, digits, punctuation,
                    whitespace)
valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}


def contains_character(password: str = "", sack: str = "") -> bool:
    has_char = False

    for char in password:
        if char in sack:
            has_char = True
            break

    return has_char


def is_valid_size(password: str = "") -> bool:
    MIN_SIZE = 6
    MAX_SIZE = 20
    password_size = len(password)

    return MIN_SIZE <= password_size <= MAX_SIZE


def get_invalid_chars():
    invalid_chars = set(punctuation + whitespace) - valid_chars
    return "".join(invalid_chars)


def get_valid_chars():
    return "".join(valid_chars)


def is_valid_password(password: str = "") -> bool:
    try:
        if not password:
            return False

        new_password = password.strip()

        if not is_valid_size(new_password):
            return False

        if not contains_character(new_password, ascii_lowercase):
            return False

        if not contains_character(new_password, ascii_uppercase):
            return False

        if not contains_character(new_password, digits):
            return False

        if contains_character(new_password, get_invalid_chars()):
            return False

        if not contains_character(new_password, get_valid_chars()):
            return False

        return True
    except:
        return False

```

The unit tests will be in `test.py` and would look like the snippet below:

```python
import unittest
from app import (contains_character, is_valid_size, is_valid_password)


class TestContainsCharacter(unittest.TestCase):
    def test_empty_password_or_and_empty_sack(self):
        self.assertFalse(contains_character())

    def test_char_i_in_str_python(self):
        self.assertFalse(contains_character("i", "python"))

    def test_str_py_in_str_python(self):
        self.assertTrue(contains_character("py", "python"))

    def test_str_python_in_str_python(self):
        self.assertTrue(contains_character("python", "python"))


class TestIsValidSize(unittest.TestCase):
    def test_empty_password(self):
        self.assertFalse(is_valid_size(""))

    def test_4_char_password(self):
        self.assertFalse(is_valid_size("pass"))

    def test_6_char_password(self):
        self.assertTrue(is_valid_size("passwd"))

    def test_16_char_password(self):
        self.assertTrue(is_valid_size("ThisIs1Password!"))

    def test_20_char_password(self):
        self.assertTrue(is_valid_size("ThisIs1Password!/+20"))

    def test_21_char_password(self):
        self.assertFalse(is_valid_size("ThisIs1Password!/+20&"))


class TestIsValidPassword(unittest.TestCase):
    def test_empty_password(self):
        self.assertFalse(is_valid_password())

    def test_password_of_size_three(self):
        self.assertFalse(is_valid_password("pas"))

    def test_password_of_size_ten(self):
        self.assertFalse(is_valid_password("Password12"))
        self.assertTrue(is_valid_password("Password1_"))

    def test_password_of_size_twenty(self):
        self.assertTrue(is_valid_password("Password12Password_$"))

    def test_password_with_invalid_special_character_semicolon(self):
        self.assertFalse(is_valid_password("Password1_;"))
        self.assertFalse(is_valid_password("Password1;"))

    def test_password_with_no_digit(self):
        self.assertFalse(is_valid_password("Password_"))

    def test_password_with_no_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD1_"))

    def test_password_with_no_uppercase(self):
        self.assertFalse(is_valid_password("password1_"))

    def test_password_without_valid_special_character(self):
        self.assertFalse(is_valid_password("Password1"))

    def test_valid_password(self):
        self.assertTrue(is_valid_password("Password1_"))
        self.assertTrue(is_valid_password("PassWord34$"))


if __name__ == "__main__":
    unittest.main()

```

Feel free to voice your opinion and if you find it wanting or not, let me know how to make it better.
