# So The newbies Created a Utils File

The `Validator` class has `validate_size`, `is_email_valid`, `email_exist`, `is_password_valid` and `is_valid_hash` as methods. We have discussed (and updated), `validate_size` and `email_exist`. Now `email_exist` is `is_existing_email`.

In the `part3`, I asked if it was okay to have a one-liner function.

## The One-Liner Function

I am not against one-liner functions because they can prove useful. Let's consider the snippet below to see if it was okay to use a one-liner function.

```python
def add_one(x: int):
    return x + 1


def add_two(x: int):
    return add_one(add_one(x))


print(add_one(12))  # -> 13
print(add_two(12))  # -> 14

```

Do you thing this is bad, considering how short `add_one` and `add_add_two` are?

> For someone who is written code in one of the Lisp-like languages would understand more.

The snippet above is actually useful because, `add_two` makes use and builds on top of `add_one`. Both `add_one` and `add_add_two` takes argument/data to operate on. So in this case, a one-liner function is useful.

## is_valid_hash

The snippet below is the `is_valid_hash` method.

```py
class Validator:

    def is_valid_hash(self, password, hashed_password):
        return bcrypt.verify(password, hashed_password)

```

The `is_valid_hash` method:

-   takes arguments
-   uses _bcrypt.verify_
-   but does not build on top of it

So should the `is_valid_hash` method be a one-liner? I don't think so. Assume we remove the function head, then what do we have? We have `bcrypt.verify(password, hashed_password)`, and we can use it directly. The `is_valid_hash` method does not build on top of `bcrypt.verify(password, hashed_password)` nor override its implementation.

## Lesson

<!-- Look into the Single Responsibility Principle of SOLID -->

I believe that, it would be better if we'd use `bcrypt.verify(password, hashed_password)` directly or we have its own separate class. It also seemed like the `is_valid_hash` method, would have disappeared into thin air, more reason we should have a separate class for it (since we need that functionality).
