# So The newbies Created a Utils File

We discussed the `generate_token` function and how I'd write it today. In this part, we will look at a snippet that was a mistake or better, a deviation. The function implementation is kind of different from the _doc string_, below:

```py
"""
Returns the number of specific characters in data that is in the sack
By default, data is an empty string and sack is an empty list
Both data and list, are iterable
If neither data nor sack is set, zero in returned
"""
```

## get_schar_count

Can you implement a function for the _doc string_ above? Give it a try without looking at mine.

We are all learning from the success and mistakes of others so do not worry or feel down if you couldn't.

Ok, my snippet at that time looks like this:

```python
def get_schar_count(data='', sack=[]):
    """
    Returns the number of specific characters in data that is in the sack
    By default, data is an empty string and sack is an empty list
    Both data and list, are iterable
    If neither data nor sack is set, zero in returned
    """
    if not data or not sack:
        return 0

    counter = 0

    for char in data:
        if char in sack:
            counter += 1

    return counter

```

I am surprised. This function completely deviates from its functionality (Comparing the _doc string_ to the actual code).

## So what does this snippet do?

To make no assumptions, let's ignore the content of the _doc string_.

-   If either data or sack is not given return `0`
-   Initialize `counter` variable with a value of `0`
-   Looping through `data` with (or using) `char` as a loop pointer, check if `char` is in `sack` then increment `counter` variable by `1` else do nothing (move to the next iteration)
-   Return `counter` at the end of the loop

From there, it is obvious what `get_schar_count` is meant to do or does.

Let me make it simple (not easier). Assume that we want the user password to contain certain characters. The password must be just lowercase alphabets and maybe a single number say `'1'` (This `1` is a string since it is part of a string - the password). Then `sack` will be, `['a', 'b', 'c', ..., 'z', 1]`. At the end of the loop, if `counter` is less than `len(data)` then the password (in this case, the `data`) provided is invalid. So the counter that is returned from the function is the number of characters in `data` that are in `sack`.

Have you noticed the conflict or the deviation yet?

## The Deviation

What do you call a function that works but does not do what it is supposed to do?

Let's have a look at the _doc string_ again.

```py
"""
Returns the number of specific characters in data that is in the sack
By default, data is an empty string and sack is an empty list
Both data and list, are iterable
If neither data nor sack is set, zero in returned
"""
```

This is like a frequency counter. A frequency counter - counts the number of unique individual elements in a `list`, `string`, etc. I think I wanted it to return a dictionary (an object) or something like that. I didn't want the user's password to have repeated characters. `get_schar_count` rather checks (counts) if the `data` supplied is valid (in the `sack`).

## Some Implementations

I came up with some implementations.

### Snippet 1

```python
def get_schar_count(data):
    schar_count = {}

    for char in data:
        if char in schar_count:
            schar_count[char] += 1
        else:
            schar_count[char] = 1

    return schar_count
```

### Snippet 2

```python
def get_schar_count_dict(data):
    schar_count = {}

    for char in data:
        char_count = schar_count.get(char, 0)
        schar_count[char] = char_count + 1

    return schar_count
```

### Snippet 3

```python
def get_schar_count(data):
    schar_count = {}

    for char in data:
        if char not in schar_count:
            schar_count[char] = 0

        schar_count[char] += 1

    return schar_count
```

### So What Is Different?

These snippets do the same thing. They are the same thing. The first could look much like the second with a little tweak.

Assuming we passed `'hello'` as `data` an output similar to that below will be generated.

```py
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

## If The Original Works, Could It Be Used?

The original snippet can be used even though it deviates from its purpose. It serves another valid purpose as mentioned above, it can be used to validate a password, in our case. That is if the function head was, `def get_schar_count(data='', sack=[]):...`

> Let me make it simple (not easier). Assume that we want the user password to contain certain characters. The password must be just lowercase alphabets and maybe a single number say `'1'` (This `1` is a string since it is part of a string - the password). Then `sack` will be, `['a', 'b', 'c', ..., 'z', 1]`. At the end of the loop, if `counter` is less than `len(data)` then the password (in this case, `data`) provided is invalid. So the counter that is returned from the function is the number of characters in `data` that are in `sack`.

From the above, we can say that the original snippet can be used to validate the user password. As far as the value returned, `counter`, is of the same size as `data`, then all the characters in `data` is in `sack`, hence, `data` is valid, else invalid.

### Re-Implementation of the Original Snippet

I would have to rewrite the original with a few changes.

```python
def is_password_valid(data='', sack=[]):
    """
    Returns True when all the characters in data are in sack else False
    By default, data is an empty string and sack is an empty list
    Both data and list, are iterable
    If neither data nor sack is set, False in returned
    """
    if not data or not sack:
        return False

    for char in data:
        if char not in sack:
            return False

    return True
```

## Lesson

I wasted my resources on this function, thinking and writing the code. If I had thought well of a use case, then the function, `get_schar_count`, would make sense to me now and ever. To avoid such headaches:

-   Write a unit test at least for your functions. This way if the function is not useful, you'd realize it and remove it from the codebase entirely.
-   Before you create a function, make sure that that functionality is needed. Now use the function in your code before implementing it. This is just like writing tests before implementation.
-   "`get_schar_count`"? What? Find a better descriptive name (I maintained it because it did the work).
-   There is a one-liner approach that to me it is good but for the sake of readability, I'd choose another approach.
    ```python
    def get_schar_count(data):
      return { char: data.count(char) for char in set(data) }
    ```
-   If you noticed, none of the snippets above modified the `data` passed to it. The `data` argument/variable was not modified. At least, in your dysfunctional code, don't modify some data.
- As a programmer, you have the privilege to be forgetful. It's okay, make use of comments, in fact, a `.md` file for comment just for some function or file, you don't know when you will come back to the code again. Again, this is just an exaggeration.
