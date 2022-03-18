# So The newbies Created a Utils File

Before anything, let's have a look at some snippets.

```python
from passlib.hash import bcrypt
from datetime import datetime


def get_bcrypt_hashed_passwd(password):
    """ hash the password using bcrypt from passlib.hash """
    return bcrypt.hash(password)


def get_current_date_time():
    """ return the current date and time """
    now = datetime.now()

    # format the datetime using
    # [month, day, year, hour, minute, sec]
    # [%B, %d, %Y, %H, %M, %S] : December 2, 1996 - 13:24:20
    # return now.strftime("A%, %d %B, %Y - %H:%M:%S")
    return now.strftime("%B %d, %Y - %H:%M:%S")


class DataSizeRange:
    """
    Set the min_range and max_range for data to evaluate valid size
    By default, min_range=6 and max_range=20
    """

    def __init__(self, min_range=6, max_range=20):
        self.min_range = min_range
        self.max_range = max_range

```

What do you think? Can you make out what these snippets do?

I was wondering if it is okay to create a function for a code that isn't repeated? I mean, during refactoring, you also do the "refactoring" when there is code duplication, right?

So, is it okay to create a function for a one-liner code? What if the function doesn't take an argument? What is the use of the `DataSizeRange` class? Do you think it should be a function? I mean, what does `DataSizeRange` do, so that we make it a function?

## The Generator Class

Well, there was a class I called, `Generator`. Let me share the content of the class below, without the method bodies so that we can have a shortcode to read.

```python
class Generator:

    def generate_token(self):
        pass

    def get_schar_count(self, data='', sack=[]):
       pass

    def get_bcrypt_hashed_passwd(self, password):
        """ hash the password using bcrypt from passlib.hash """
        # use bcrypt to hash the password
        return bcrypt.hash(password)

    def get_current_date_time(self):
        now = datetime.now()
        return now.strftime("%B %d, %Y - %H:%M:%S")
```

`generate_token` and `get_schar_count` were discussed in `part1` and `part2`. So have you seen the reason why I asked, should one-liner functions exist in our codebase?

Let's update the `Generator` class with the changes made in the other parts.

```python
class Generator:

    def generate_token(self, token_size=6):
        pass

    def is_password_valid(self, data='', sack=[]):
       pass

    def get_bcrypt_hashed_passwd(self, password):
        return bcrypt.hash(password)

    def get_current_date_time(self):
        now = datetime.now()
        return now.strftime("%B %d, %Y - %H:%M:%S")
```

Do you think `is_password_valid` should exist in the `Generator` class?

## The Validator Class

The `Validator` class has `validate_size`, `is_email_valid`, `email_exist`, `is_password_valid` and `is_valid_hash` as methods.

We will discuss the first method, which is `validate_size`.

So we will have the `Validator` class below:

```python
class Validator:
    ...

```

### The `validate_size` Method

```python
class Validator:

    def validate_size(self, data, dataSizeRange):
        """
        Pass DataSizeRange Object to the validate_size method with the required range
        Returns True if size (len) of data is inclusively (both ends) in range else, False
        """
        return dataSizeRange.min_range <= len(data) <= dataSizeRange.max_range
```

Does this method sound like the description of the original `is_password_valid` method? Well, they sound the same in "name" but not functionality.

The `validate_size` method checks if the `data` passed (argument) falls within the _min_ and _max_ size as defined by the `DataSizeRange` Object.

Wouldn't it be better if `validate_size` was `is_valid_size` or `is_size_valid` since it returns a boolean?

For the `dataSizeRange` parameter, look at the `DataSizeRange` class above.

### The `email_exist` Method

```python
from http.client import HTTPSConnection as httpConn

class Validator:

    def email_exist(self, domain):
        """
        ping the domain's server to see if the domain exists
        using http.client and get a response of 200 OK
        """

        conn = httpConn(domain)
        conn.request("HEAD", "/")
        res = conn.getresponse()

        if res.status != 200 or res.reason != "OK":
            return False
        return True
```

The `email_exist` method does exactly what its **doc string** says. We assume the email is valid/exist if a ping to the domain returns a `200` status code.

What did you notice about the `email_exist` method? (If you don't know how the import words are, it's okay. Ignore it. Assume it returns a status code of `200` on success, anything else is an error.

These are a few things I noticed.

-   Obviously, the name of the method doesn't indicate it will return a boolean.
-   Even if we are to maintain the name, we have to add an `'s'` to it, as in `email_exists`. It sounds well with the `if` keyword. `if email_exists( ... )`.
-   The `email_exist` method doesn't say the email exists but the domain. So it seems we can change the name to `domain_exists` but let's maintain the old name.
-   The response, if the `status` code is `200` the the `reason` will be `"OK"`

### Refactor of the `email_exist` method

```python
from http.client import HTTPSConnection as httpConn

class Validator:

    def is_existing_email(self, domain):
        """
        ping the domain's server to see if the domain exists
        using http.client and get a response of 200 OK
        """

        conn = httpConn(domain)
        conn.request("HEAD", "/")
        res = conn.getresponse()

        return res.status == 200
```

### What Would Make The Above Snippet OK

It was nice when I was using this method/function for email validation. Today, I realized that some domains/sites are redirected and as such, the response we'd get would have a `301` status. Visit [gmail.com](gmail.com), [google.com](google.com) and some others and you'd see that the URL changes to that with `https`.

We can use the `or` operator to also account for redirect as in, `return res.status == 200 or res.status == 301`. We could also do, `return res.status in [200, 301]`

## Lesson

There number one lesson here would be to often update yourself with the stack you are using (Don't jump to it but be updated).

Now regarding the snippet, don't change the code if:

-   you have not been permitted to do so (by the Organization, it is not your code)
-   you are leaving the organization (codebase)
-   it is premature
-   you don't understand what you have to change and what changes to make
-   it is working and you are happy (this is like a principle that will make me smile)
