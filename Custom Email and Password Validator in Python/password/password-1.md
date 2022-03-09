# Custom Password Validation in Python (Function for password validation)

These posts will be in three parts.

1. Function for password validation
2. Refactoring the function for password validation
3. Unit test the function for password validation

Who cares about custom password validation? If some libraries/modules can effortlessly validate our passwords, is there a need to (re)write one? Why?

What do we say is a strong password? How is a strong password structured? Can we define a strong password? Are strong passwords even important? Is the security of our application any better with secure passwords?

The purpose of asking these questions is so that we can all, at least, be on the same page - agree that we need secure and safe passwords. I am not a software security expert or engineer, so don't trust me.

## The Structure Of A Secure Password

As I said earlier, "I am not a software security expert or engineer, so don't trust me". I meant it. Since the idea of the structure of a password may be a preference or based on requirements, I think that at a point, we should all agree that a password should (or must) satisfy most of these conditions. (These are my conditions, you are free to add and remove).

-   No leading or trailing white spaces - so we strip them off
-   Should be between 6 to 20 characters long
-   Must exclude any of these, `` %;`<>\/{}[]+=?&,:'"  `` and blank space
-   Must have at least one special symbol. `!@#$^&()_.-`.
-   Must have at least one number.
-   Must have at least one lowercase character.
-   Must have at least one uppercase character.

We will implement a function to take care of each of these conditions.

## The Function

Usually, it is hard for developers to name "things" in their code. I add a keyword from the function description to the function name. Our function validates a password. We can name it a `password_validator`. `password_validator` is a noun. We need a verb. `validate` or `validate_password` will do. We expect a `bool` from the function. `is_valid` or `is_valid_password` sounds "ok". The latter sounds better with a context, which is alright since we are using a function and not a class. The former would be better if we were to implement a class. From here on our function name is `is_valid_password`.

### Function Definition

```python
def is_valid_password(password):
    pass
```

We would start with this function definition without a body/implementation. The `pass` keyword means we would implement the body later.

### No Trailing Spaces

In a form, there maybe be a chance that the submitted data has some space with it. `newline`, which is `enter` may submit the form. `tab`, would go to the next input field. `Space` will just add space so we have to strip/trim it. In python, we use the `strip` method to remove spaces from the password (a password is a string object).

```python
def is_valid_password(password):
    new_password = password.strip()
```

As you can see, the password variable (parameter) was not modified. This is a good practice not to directly modify data passed as an argument.

### Must Be Between 6 To 20 Characters Long

Does the size of the password matter, security-wise? Yes, it matters a lot. Sat we have a one-character-password. This password is limited to the alphabetic letters in the range, `[A-Za-z]`. Guess how long it will take a python script to crack it?

I would say that a password should be between `6` to `20` characters long. I believe `8` should be a minimum. The only issue here is that the user must remember a sequence of `8` or so characters for a password.

```python
def is_valid_password(password):
    ...

    if len(new_password) < 6 or len(new_password) > 20:
        return False
```

In the above snippet, if the password length is less than six or twenty characters, the function returns `False`. Now we have two magic numbers, numerical literals, we can easily replace them with some constant variables.

Which name will be better, `MIN_SIZE` or `MIN_PASSWORD_SIZE`? The latter has a context. It makes it a better name in my opinion.

The `is_valid_password` function name itself has a context so in a way, we don't have to be "sticky" with "contexting". It makes `MIN_SIZE` a more suitable option.

```python
def is_valid_password(password):
    ...

    MIN_SIZE = 6
    MAX_SIZE = 20
    password_size = len(new_password)

    if password_size < MIN_SIZE or password_size > MAX_SIZE:
        return False
```

### Must Have A Special Character

There are characters other than letters and numbers that should also be included and excluded from a password.

Characters to:

-   include: `!@#$^&()_.-`
-   exclude: `` %;`<>\/{}[]+=?&,:'"``

All other symbols not accounted for should be excluded from the special characters. We would use some import from the `string` module.

```python
from string import punctuation, whitespace

def is_valid_password(password):
    ...

    valid_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')'}
    invalid_chars = set(punctuation + whitespace) - valid_chars
```

To account for the other symbols to exclude, we added punctuations and whitespace then we remove all valid characters. Now we have invalid characters. If any of the invalid characters are found in the password passed, then the password is invalid so we return `False`.

```python
from string import punctuation, whitespace

def is_valid_password(password):
    ...

    for char in invalid_chars:
        if char in new_password:
            return False
```

### Must Have At Least One Number

It is not bad to have a number in a password. Let's check if the password has a number. We would import `digits` from the `string` module.

```python
from string import digits

def is_valid_password(password):
    ...

    password_has_digit = False

    for char in password:
        if char in digits:
            password_has_digit = True
            break

    if not password_has_digit:
        return False
```

We set a flag (something that can be turned/switched on/off), `password_has_digit` and we set it to `False`. We assume that the password has no number in it. We loop through the password and check if a character in the password is a number. If a character is a number, we set `password_has_digit` to `True` and we `break` from the loop. Finally, we check if the flag we set is `False` to return `False` from the function as a password without a number is invalid (in our case).

### Must Have At Least One Lower and Upper Case Character

Keystrokes from the keyboard are lower cases. We either have to hit the `caps lock` or hold down the `shift` key to enter an upper case character.

Let's check for a lower case character in our password. We can manually enter the lower case characters into a string or list but we can import them from the string module. We did the same for `digits, punctuation and whitespace`.

```python
from string import ascii_lowercase, ascii_uppercase

def is_valid_password(password):
    ...

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
```

### Finally

We will return `True` when these requirements are met.

```python
def is_valid_password(password):
    ...

    return True
```

## Conclusion

Our code will like the snippet below when we assemble it.

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

You better cross your fingers. It is not battle-tested. We would get into details and reveal some bugs in the second part of the post. The next post will be on Refactoring the function for password validation.
