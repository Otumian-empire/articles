# So The newbies Created a Utils File

As a newbie, don't take "these" software engineering practices as a trophy. You hear things like, "the code smells", "DRY", "KISS" and others. Seriously, don't. I mean, you could after you are done with your project and everything is working and you are happy. If you are happy, don't even touch the code. You are a newbie and we newbies love things when they are working. (Isn't that right?)

Reading about software engineering practices and what have you, as a newbie, can be very influential sometimes. A three hours practice project can become a week old if you are "lucky" - that is, you had another eye to tell you what went wrong. You could even hide your project in the 🗑️. (I meant you delete it because you don't want to be known as the guy with the most uncompleted projects)

Earlier on, I learnt you should not mix your _helping functions_ with the _business logic_. You have to separate them. This is called, separation of concerns. Ok!

He was like, "Hey bro! That is not a very good practice. Create a new file for your utility functions". So I created a file, called it `utils.py` and went for a water break. (I went to sleep, I was a newbie, what did you expect? Did I regret snoozing? Nah! I enjoyed it.). 

> The lesson here, read more about the concept and see how it should and could be used in your project. By this, how do you understand and interpret the concept? How does the concept fit into your current project?

## The Sign-Up and Login Form

What makes one newbie more suitable for an entry-level job than another is the tendency to explore - experiment, break and fix.

This is was a practice project that swell up to become a full-blown project. I was just creating a sing up and login functionality and it became a whole [project][24pill-code-flask]. Do you remember or know anything about [cs50-flask] by David Malan, Harvard? Maybe this link was not the one I watched, it was [cs50-harvard].

## The Helper File

The file contains a whole lot of functionalities.

### Generate Random Characters

There is a function for generating tokens for email and password updating.

```python
from string import ascii_letters, digits
from random import randint

def generate_token():
    TOKEN_LENGTH = 6
    token = ""

    code_alphabet = ascii_letters + digits + "_"

    max = len(code_alphabet)

    for i in range(TOKEN_LENGTH):
        token += code_alphabet[randint(0, max - 1)]

    return token
```

How is this function working?

- `ascii_letters` returns `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`.
- `digits` returns `0123456789`.
- `randint` is a function that takes a `min` and `max` inclusive argument.
- This function, `generate_token`, takes no argument.
- `TOKEN_LENGTH` is the number of characters I want to generate. In this case, it is `6`.
- `token` is an initialized string variable to hold the random characters to be generated.
- `code_alphabet` is a string concatenation of `ascii_letters`, `digits` and an `_`.
- `max` is assigned the length of `code_alphabet`. `max` was a very bad name. Do you know why as a newbie?
- using the `for-range` looping construct, looping `TOKEN_SIZE` times, indexing `code_alphabet` using the `randint` function passing `0` and `max - 1` as arguments. We want to be able to index the first element from `code_alphabet` so we passed `0` and `max - 1` so that the value would be in the range of index else we'd get an `IndexError`.
- The random character from `code_alphabet[randint(0, max - 1)]` is add to `token`
- `token` is returned as a result

### What will I change if I were to rewrite `generate_token` today?

- To make use of the `generate_token` function somewhere, I'd rather pass the desired token size to it. I'd make it by default, `6` characters. So the function definition would look like, `def generate_token(token_size=6): ...`
- I will rename `code_alphabet` to `token_source`
- I will rename `max` to `token_source_length` or `token_source_size`. If were look at `token += code_alphabet[randint(0, max - 1)]`, we would realize that, `max - 1` was used as the endpoint for the `randint` function. So we can rather name it `end_point`. So I will let `end_point = len(token_source) - 1`
- Assign `start_point` the value, `0`. Pass `start_point` as the first argument in the `randint` function.
- I will use "string" comprehension and the string join method to create the token. I usually don't favour this syntax if it makes reading the code a headache.
- Instead of assigning the generated token to `token` and then returning `token` after the loop, I will just return the generated token. This way I won't have to initialize `token`.
- A linter will warn you that there is an unused variable if the variable was declared or initialized but was never used. So instead of using a variable in the `for-range` construct, I'd use `_` - _a throw-away-variable_.

The rewritten function will look like the snippet below.

```Python
from string import ascii_letters, digits
from random import randint

def generate_token(token_size=6):
    token_source = ascii_letters + digits + "_"

    start_point = 0
    end_point = len(token_source) - 1

    return "".join(
        token_source[randint(start_point, end_point)]
            for _ in range(token_size)
    )
```

## Lesson

Do you remember, "with power comes great responsibilities"? Some say the inverse. Well, with experience comes a different code. This does not mean there won't be flaws. A flaw may not necessarily be a bug or error. A design approach could be a flaw. The readability issue could be a flaw. Complexity could be a flaw. What changes would you make in the snippet above?

#

[24pill-code-flask]: https://github.com/Otumian-empire/24pill-code-flask
[cs50-flask]: https://www.youtube.com/watch?v=x_c8pTW8ZUc
[cs50-harvard]: https://cs50.harvard.edu/college/2021/fall/
