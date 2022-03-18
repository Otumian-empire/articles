# Custom Email Validation in Python (Function for email validation)

What should we consider a valid email? Consider these emails below to see if they are valid. Would you accept such emails even if they are valid?

```
1. "very.unusual.@.unusual.com"@example.com
2. "very.(),:;<>[]\".VERY.\"very@\ \"very\".unusual"@strange.example.com
3. "#!$%&'*+-/=?^_`{}|~@example.org"
4. "()<>[]:,;@"!#$%&\'-/=?^_`{}| ~.a"@example.org
```

It turns out they are valid but should we accept them? You can also read on it [here][link].

## Some Valid Emails

Let's have a look at some valid emails. These emails are from [here][link].

-   `prettyandsimple@example.com`
-   `very.common@example.com`
-   `disposable.style.email.with+symbol@example.com`
-   `other.email-with-dash@example.com`
-   `x@example.com`
-   `"much.more unusual"@example.com`
-   `"very.unusual.@.unusual.com"@example.com`
-   `"very.(),:;<>[]\".VERY.\"very@\ \"very\".unusual"@strange.example.com`
-   `example-indeed@strange-example.com`
-   `admin@mailserver1 (local domain name with no top-level domain)`
-   `` #!$%&'\*+-/=?^\_`{}|~@example.org ``
-   `` "()<>[]:,;@\\"!#$%&'-/=?^\_`{}| ~.a"@example.org ``
-   `" "@example.org`
-   `example@localhost`
-   `example@s.solutions`
-   `user@com`
-   `user@localserver`
-   `user@[IPv6:2001:db8::1]`

## Some Invalid Emails

-   `Abc.example.com` - there is no `@` character
-   `A@b@c@example.com` - only one @ is allowed outside `quotation marks
-   `a"b(c)d,e:f;gi[j\k]l@example.com` - none of the special characters in this local part are allowed outside quotation marks
-   `just"not"right@example.com` - quoted strings must be dot separated or the only element making up the local part
-   `this is"not\allowed@example.com` - spaces, quotes, and backslashes may only exist when within quoted strings and preceded by a backslash
-   `this\ still\"not\allowed@example.com` - even if escaped (preceded by a backslash), spaces, quotes, and backslashes must still be contained by quotes
-   `john..doe@example.com` - there are two dots before `@`
-   `john.doe@example..com` - there are two dots after `@`
-   `a valid address with a leading space`
-   `a valid address with a trailing space`

## Let's Set Limitations On The Emails

A normal email would look something more like `username@domain.com`. This email is of three parts.

-   `username` - account name or the local part
-   `@` - at sign
-   `domain.com` - domain or server name with an extension

### Local part

The username part of the email address may use any of these ASCII characters:

-   Uppercase and lowercase English letters - `[a-zA-Z]`
-   Digits - `[0-9]`
-   Special Characters - `` ! # $ % & ' \* + - / = ? ^ \_ ` { | } ~ . ``
    -   We will accept, `- _ .`
    -   The dot character, `.`, must not the first or last character
    -   It must not appear two or more times consecutively
-   all characters will be changed to lower case. So `HellO@gmail.com` will be the same as `hello@gmail.com`

## The Function

It's time to write some code.

We would start with the function definition:

```py
def is_email_valid(email):
    pass

```

### Allowed Valid Characters

We would accept `'-', '_', '.'` as valid characters and any other that is not enclosed in a quote is not accepted.

Let's import punctuation and whitespace from the string module.

```py
from string import punctuation, whitespace

def is_email_valid(email):
    valid_chars = {'-', '_', '.'}
    invalid_chars = set(punctuation + whitespace) - valid_chars

```

### No Leading Or Ending Space

We have to strip or trim the email of leading or ending space.

```py
def is_email_valid(email=""):
    ...

    stripped_email = email.strip()

```

### Email Must Have Only One @ Character

An email must have an `@` and there must be only one `@`.

```py
def is_email_valid(email=""):
    ...

    # email must have @
    if "@" not in stripped_email:
        return False

    # there must be one @
    if stripped_email.count("@") != 1:
        return False

```

### Get The Local And Domain

We have to split the email at the `@` character to get the local and the domain.

```py
def is_email_valid(email=""):
    ...
    # split the email into local and domain part
    local, domain = stripped_email.split("@")

```

### Invalid characters must be in quotes

Apart from `-, _ and .` all other characters must be in double quotes in the local.

```py
def is_email_valid(email=""):
    ...
    for char in invalid_chars:
        if (
            char in local
            and (not local.startswith('"')
                 or not local.endswith('"'))):
            return False

```

### No consecutive dots

We will get the first dot then the next.

```py
def is_email_valid(email=""):
    ...
    if "." in local:
        try:
            dot_position_in_local = local.index(".")

            if local[dot_position_in_local + 1] == ".":
                return False
        except:
            return False

```

### Must not start or end with do

The local must not start or end with a dot.

```py
def is_email_valid(email=""):
    ...
    if local.startswith(".") or local.endswith("."):
        return False

```

### Domain Must Not Start Nor End with a Hyphen or Dot

The domain can not have a dot nor hyphen as the first or last character.

```py
def is_email_valid(email):
    ...
    if domain.startswith("-") or domain.endswith("-"):
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False
```

### This is enough

Finally, we can return `True` since all the validation is checked. This validation would or may fail for some emails. This function is for the sake of education and fun.

```py
def is_email_valid(email):
    ...
    return True
```

## Conclusion

Minimally, this function works around `valid_chars = {'-', '_', '.'}`. You can say it rather checks for invalid emails. It is okay.

> If you can not work hard to move forward, work harder not to move back.

The snippet we now have is:

```py
def is_email_valid(email):
    valid_chars = {'-', '_', '.'}
    invalid_chars = set(punctuation + whitespace) - valid_chars

    stripped_email = email.strip()

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
```

Watch out for the next two articles on refactoring and testing this function for validating emails.

I have a three-part series on password validation, you can check them out.

{% post https://dev.to/otumianempire/custom-password-validation-in-python-function-for-password-validation-376a %}

{% post https://dev.to/otumianempire/custom-password-validation-in-python-refactoring-the-function-for-password-validation-2i95 %}

{% post https://dev.to/otumianempire/custom-password-validation-in-python-unit-test-the-function-for-password-validation-4l7b %}

#

[link]: https://stackoverflow.com/questions/2049502/what-characters-are-allowed-in-an-email-address
