# Custom Password Validation in Python (Refactoring the function for password validation)

These posts will be in three parts.

1. Function for password validation
2. Refactoring the function for password validation
3. Unit test the function for password validation

This is the second part of the Custom Password Validation in Python series. In this post, we will be looking at, Refactoring the function for password validation.

There are parts of the code that needs a little "touch" here and there. Here are a few things I think we can modify or improve.

This snippet below was the final implementation we had.

{% post https://dev.to/otumianempire/custom-password-validation-in-python-function-for-password-validation-376a %}

```python
from string import (
    punctuation, whitespace, digits,
    ascii_lowercase, ascii_uppercase)


def is_valid_password(password):
    new_password = password.strip()

    MIN_SIZE = 6
    MAX_SIZE = 20
    password_size = len(new_password)

    if password_size < MIN_SIZE or password_size > MAX_SIZE:
        return False

    valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
    invalid_chars = set(punctuation + whitespace) - valid_chars

    for char in invalid_chars:
        if char in new_password:
            return False

    password_has_digit = False

    for char in password:
        if char in digits:
            password_has_digit = True
            break

    if not password_has_digit:
        return False

    password_has_lowercase = False

    for char in password:
        if char in ascii_lowercase:
            password_has_lowercase = True
            break

    if not password_has_lowercase:
        return False


    password_has_uppercase = False

    for char in password:
        if char in ascii_uppercase:
            password_has_uppercase = True
            break

    if not password_has_uppercase:
        return False

    return True
```

## Refactoring

-   The password parameter, what is its type? When I hovered on it in `vscode`, it said `Any`. We expect a `string` password and not `Any`. What do we do then?

    -   Adding type annotation solves the parameter type issue (it contributes to the documentation).
    -   I thought of passing a default value to the parameter (when no argument is passed to the function).

    ```python
    def is_valid_password(password: str = "") -> bool:
        ...
    ```

-   What happens when no argument is passed? The part of the code that checks for the `MIN_SIZE` and `MAX_SIZE` will take care of not passing an argument by returning `False`. We can return `False` when an argument is not passed.

    ```python
    def is_valid_password(password: str = "") -> bool:
        if not password:
            return False
        ...
    ```

-   Consider the snippet below.

    ```python
    password_has_something = False

    for char in password:
        if char in somethings:
            password_has_something = True
            break

    if not password_has_something:
        return False
    ```

    Snippets like this have appeared several times. We can create a function for this snippet.

    The issue is that there is another similar snippet.

    ```python
    for char in invalid_chars:
        if char in new_password:
            return False
    ```

    If we can change this snippet to look and feel like the others, then the same function would work for this snippet too.

    ```python
    password_has_invalid_chars = False

    for char in new_password:
        if char in invalid_chars:
            password_has_invalid_chars = True
            break

    if password_has_invalid_chars:
        return False
    ```

-   In python, we can create a function inside a function. This function becomes local to the function it is within. The problem would be that we can not test the local function directly. For the sake of testing, we put all functions outside the `is_valid_password` function.

    ```python
    def contains_character(password: str = "", sack: str = "") -> bool:
        has_char = False

        for char in password:
            if char in sack:
                has_char = True
                break

        return has_char
    ```

-   Let's update those parts of the `is_valid_password` function.

    Now snippets like this:

    ```python
    password_has_something = False

    for char in password:
        if char in somethings:
            password_has_something = True
            break

    if not password_has_something:
        return False
    ```

    Will become:

    ```python
    if not contains_character(password, somethings):
        return False
    ```

    This is will different though for the invalid characters, `invalid_chars`. When there is an invalid character, return `False`. So when the function returns `True`, return `False`.

-   It seems we can abstract `password_size < MIN_SIZE or password_size > MAX_SIZE`. `password_size < MIN_SIZE or password_siz > MAX_SIZE` makes use of `MIN_SIZE` and `MAX_SIZE`. Do we pass them as arguments? No. I think we shouldn't. We should rather make them local to the (new) function.

    Let's create this function, `is_valid_size`.

    ```python
    def is_valid_size(password: str = "") -> bool:
        MIN_SIZE = 6
        MAX_SIZE = 20
        password_size = len(password)

        return password_size < MIN_SIZE or password_size > MAX_SIZE
    ```

    This will return `True` if `password_size < MIN_SIZE` and also when `password_size > MAX_SIZE`. The value we expect from this is `False`. That is our true success. That is when the password is in the desired range. We should write functions that return `True` on success and `False` on failure. So our new function will be better if we return `password_size >= MIN_SIZE and password_size <= MAX_SIZE`. It is the same as `MIN_SIZE <= password_size <= MAX_SIZE`. The new function becomes:

    ```python
    def is_valid_size(password: str = "") -> bool:
        MIN_SIZE = 6
        MAX_SIZE = 20
        password_size = len(password)

        return MIN_SIZE <= password_size <= MAX_SIZE
    ```

-   We can also let a function call return the invalid characters. The invalid characters are `string` but we have a `set`. I made `valid_chars` a `set` so that I don't have to cast it to a set before using it.

    ```python
    valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
    invalid_chars = set(punctuation + whitespace) - valid_chars
    ```

    We'd convert the above snippet in:

    ```python
    def get_invalid_chars():
        valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
        invalid_chars = set(punctuation + whitespace) - valid_chars

        return "".join(invalid_chars)
    ```

    We would then update the function with the changes made.

-   What if the user or the data received is not a `string`? What if it is a `list` or `set` or even an `int`? The best way is to use the `try and except` clause. We can return `False` on all `Exceptions`.

## The Final Code

This is what we have laboured towards.

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

## Conclusion

We can still make changes when we are writing tests. We should have written the test first but, "you know". The next post will be on, Unit test the function for password validation. There is more refactoring to do.
