# Prerequisite for Data Structures and Algorithms in Python

Whether it is _Data Structures_ or _Algorithms_ first, it is still the same.

We would look briefly at:

- Variables and expressions
- Functions
- Condition
- Iteration

## Variables and expressions

Variables are of the form, `var_name = value`. There is no semicolon.

These are some examples:

```py
>> name = "daniel"
>> age = 34
>> height = 6.6
>> numbers = [1, 2, 3, 4, 5]
>>
```

An expression will result to a value or "return" a value.

```py
>> 2 + 3
>>
>> import datetime
>>
>> currentYear = datetime.datetime.now().year
>> age = 34
>> yob = currentYear() - age
>>
>> # some operators
>> # +,  -,  /, *, **, %
>> # >, <, ==, <=, >=,  !=
>>
```

## functions

This is how we would create a function in python:

```py
def func_name([parameters]):
    # func_body

```

A function that prints 3 to the screen:

```py
def print_number():
    print(3)

print_number()
# 3

```

A function that returns 3

```py
def returnNumber():
    return 3

res = returnNumber()
print(res)
# 3

```

A function a takes with a parameter `a`. We add 2 to `a` and return the results:

```py
def addTwo(a):
    b = a + 2
    return b

res = addTwo(3)
print(res)
# 5

```

## Decision structure

An if statement is of the form:

```py
if condition:
    # if-body
```

The body/block of the if statement is executed when the condition evaluates to `True`

```py
age = 20
res = age > 18

if res:
    print(age)

# prints 20 because age, 20, is greater than 18

```

We can add an `else` part to the `if` statement. This is the part of the code that is executed when the condition evaluates to `False`.

```py
if condition:
    # if-body
else:
    # else-body

```

This is an if-else statement:

```py
age = 12
res = age > 18

if res:
    print(age)
else:
    print("sorry, age must be above 18")
# prints, sorry, age must be above 18, since age is less than 18

```

We can use the `and` and `or` to compound logical expressions. `and` and `or` are known as logical operators.

```py
age = int(input("Enter age: "))

if age > 18 and age % 2 == 0:
    print("Age is greater than 18 and it is even")
else:
    print("age must be greater than 18 and it is even")

```

We can also nest the if-else statements

```py
age = int(input("Enter age: "))

if age > 18:
    if age % 2 == 0:
        print("Age is greater than 18 and it is even")
   else:
        print("Age must be even")
else:
    print("age must be greater than 18")
```

## Iteration

This is known as looping. We for loop and while-loop in python

This is a for-loop that prints numbers from 0 to 5 (exclusive).

```py
# for i in range(5):
# for i in range(0, 5):
for i in range(0, 5, 2):
    print(i)
```

We can print the content of a list using a for-loop

```py
numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(i)

```

Loops are index-based and we can pass the size of the list as an argument to the range function to determine where the loop ends.

```py
for i in range(len(numbers)):
    print(numbers[i])

```

We can also nest for loops:

```py
numbers = [1, 2, 3, 4, 5]

for i in numbers:
    for j in numbers:
        print(i * j)

```

This is how we write for loops in python:

```py
while condition:
    # while-body

```

Let print from 0 to 5 inclusive

```py
start = 0
end = 5
step = 1

# this is same as the above
# start, end, step = 0, 5, 1

while start <= end:
    print(start)
    start = start + step
    # start += step

```

We can use a while loop to loop through a list

```py
numbers = [1, 2, 3, 4, 5]
i = 0

while i < len(numbers):
    print(numbers[i])
    # i+= 1
    i = i + 1

```

We can nest while loops too

```py
i = 0

while i < 5:
    j = 0

    while j < i+1:
        print(i*j)
        j += 1

    i += 1

```

## So, what is next?

- [python series][python-series]
- [java series][java-series]

So what is next? A series on `Algorithms and Data structures in Python`. It is more or less `Introduction to data structures and algorithm 1`. We would be using python. This means we can use another language. Stay tuned as they say. Seriously stay tuned.


#
[python-series]: https://dev.to/otumianempire/series/9932
[java-series]:https://dev.to/otumianempire/series/17225