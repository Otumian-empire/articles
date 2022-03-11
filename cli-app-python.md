# Arithmetic on the Command-line - Clirithmetic

## Introduction

Adding numbers is one thing but doing it on the command-line is another. `Clirithmetic` combines the CLI as the front-end and python to write the back-end to perform binary arithmetic operations such as addition, subtraction, division, multiplication, modulo and exponents. We shall separate the back-end from the front-end so to make our code manageable and easy to maintain.

## Content

### The Back-end

The Back-end as the front-end is quite simple to implement. With some knowledge of python, this would be easy to read and understand. Lets create a file called `backend.py` for our backend code. It would be easier if we use functions. In hope of expanding `Clirithmetic` we better use a class.

```python
# backend.py
class Backend:

    def __init__(self, params):
        self.operator, self.operand1, self.operand2 = params
```

In the code above, is a class in our `backend.py` file called `Backend` with a constructor that accepts a list, made up of the operator and the two operands.

```python
# backend.py
class Backend:

    ...

    def add(self):
        return self.operand1 + self.operand2

    def mult(self):
        return self.operand1 * self.operand2

    def subt(self):
        return self.operand1 - self.operand2

    def div(self):
        return self.operand1 / self.operand2

    def mod(self):
        return self.operand1 % self.operand2

    def exp(self):
        return self.operand1 ** self.operand2
```

The code above defines methods (functionalities for the class) to perform the arithmetic operations. These function can be read easily and understood but what problems are we getting into?

So, how are we going to know which method to call based on the operation passed? Let's create another method called `eval` in the `Backend` that would determine which function to call based on the operator passed. The truth is that the `parser` would rather pass the index of the operator rather than the character operator. This makes it easier to determine the method to call. We shall discuss and implement the parser later.

```python
# backend.py
class Backend:

    ...

    def eval(self):
        # the operator is passed as int from the parser
        # this is the index of the operation needed
        operations = [self.add, self.subt,
            self.mult, self.exp, self.div, self.mod]
        operation = operations[self.operator]

        return operation()
```

### The Parser

We know the function to call based on the operator but how are we going to do that? Let's say we need a parser - this parser's job is to break the input we shall take from the CLI into the operator and the two operands. Also, we would use this same parser to catch any wrong data that is passed. We need only the operator to be a string and the operands as either integer or float. So the function of the parser is to:

-   check if there are three values in params
-   check if the first value of params is the operator
-   check if the second and third value of params is a type of float or integer
-   make the second and third value of params the first and second operands
-   check for zero division errors
-   check for value error
    -   operator must be either of +, -, \*, \*\*, /, or %
-   pass the index of the operator instead of the operator character
-   raise an exception and exit when there is an error
-   return the parsed values

We can debate on whether to add the parser as a method to the `Arithmetic class` or make it a stand-alone function. It is easier without tweaking, to make the parser a function than a method of the class. I think it can be done. What do you think?

```python
# parser.py
# data from the CLI is a list - params
# the parser shall also return a list if the parsing
# was successful else raise an error and exit with an
# error message

import sys

# destructure param
# operator, first operand, second operand = param


def parser(params=[]):
    operators = ['+', '-', '*', '**', '/', '%']

    # an operand can only be  `int` or `float`
    operand_types = [int, float]

    try:
        # only 3 parameters are needed
        if len(params) != 3:
            message = "In essence, an operator and two number"
            message += " operands are required. Eg: + 2 4.6"
            raise ValueError(message)

        if not params[0] in operators:
            raise ValueError(f"Unknown operator, choose from {operators}")

        if (type(params[1]) in operand_types and
                type(params[2]) in operand_types):
            raise ValueError(f"A number is required as operand")

        parsed_params = [params[0], float(params[1]), float(params[2])]

        if parsed_params[0] in operators[4:] and parsed_params[2] == 0:
            message = "None zero second operand is required for division"
            raise ZeroDivisionError(message)

        # pass the index of the operator rather than the character
        # we shall use the index to easily determine the operation
        # to call using few or not if statements
        parsed_params[0] = operators.index(parsed_params[0])

    except Exception as err_message:
        print(err_message)
        sys.exit()

    return parsed_params


```

### App

The front-end has to do with the CLI. Now we shall connect the CLI to the back-end. Create a file, `app.py`. In this file, we shall take the input from the CLI and use the parser function we wrote to parse it, then call the back-end to evaluate it. Finally, we print the result to the screen.

```python
# app.py
import sys
from parser import parser
from backend import Backend


if __name__ == "__main__":

    # sys.argv[0] is the file - app.py
    params = parser(sys.argv[1:])

    app = Backend(params)
    print(app.eval())
```

Always, the first element of `sys.argv` is the file. All that we have done here is to slice the list (sys.argv) from the second element then parse it with our parser. We create a Backend instance, pass the parsed params and then call eval().

### Full code and sample output

#### Back-end

```python
# backend.py
class Backend:

    def __init__(self, params):
        self.operator, self.operand1, self.operand2 = params

    def add(self):
        return self.operand1 + self.operand2

    def mult(self):
        return self.operand1 * self.operand2

    def subt(self):
        return self.operand1 - self.operand2

    def div(self):
        return self.operand1 / self.operand2

    def mod(self):
        return self.operand1 % self.operand2

    def exp(self):
        return self.operand1 ** self.operand2

    def eval(self):
        # the operator is passed as int from the parser
        # this is the index of the operation needed
        operations = [self.add, self.subt,
                      self.mult, self.exp, self.div, self.mod]
        operation = operations[self.operator]

        return operation()
```

#### Parser

```python
# parser.py
# data from the CLI is a list - params
# the parser shall also return a list if the parsing
# was successful else raise an error and exit with an
# error message

import sys

# destructure param
# operator, first operand, second operand = param


def parser(params=[]):
    operators = ['+', '-', '*', '**', '/', '%']

    # an operand can only be `int` or `float`
    operand_types = [int, float]

    try:
        # only 3 parameters are needed
        if len(params) != 3:
            message = "In essence, an operator and two number"
            message += " operands are required. Eg: + 2 4.6"
            raise ValueError(message)

        if not params[0] in operators:
            raise ValueError(f"Unknown operator, choose from {operators}")

        if (type(params[1]) in operand_types and
                type(params[2]) in operand_types):
            raise ValueError(f"A number is required as operand")

        parsed_params = [params[0], float(params[1]), float(params[2])]

        if parsed_params[0] in operators[4:] and parsed_params[2] == 0:
            message = "None zero second operand is required for division"
            raise ZeroDivisionError(message)

        # pass the index of the operator rather than the character
        # we shall use the index to easily determine the operation
        # to call using few or not if statements
        parsed_params[0] = operators.index(parsed_params[0])

    except Exception as err_message:
        print(err_message)
        sys.exit()

    return parsed_params
```

#### Front-end

```python
# app.py
import sys
from parser import parser
from backend import Backend


if __name__ == "__main__":

    # sys.argv[0] is the file - app.py
    params = parser(sys.argv[1:])

    app = Backend(params)
    print(app.eval())
```

#### Sample output

```sh
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py
In essence, an operator and two number operands are required. Eg: + 2 4.6
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py  + 23 56
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py  + 23 56
79.0
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py  + 23
In essence, an operator and two number operands are required. Eg: + 2 4.6
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py  + 23 0
23.0
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py  / 23 0
None zero second operand is required for division
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py  % 23 0
None zero second operand is required for division
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py + 2 4
6.0
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py - -3 5
-8.0
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py ** -3 5
In essence, an operator and two number operands are required. Eg: + 2 4.6
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py '**' -3 5
-243.0
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py % -3 5
2.0
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py / 22 7
3.142857142857143
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py // 22 7
Unknown operator, choose from ['+', '-', '*', '**', '/', '%']
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py // 22
In essence, an operator and two number operands are required. Eg: + 2 4.6
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py /+ 22
In essence, an operator and two number operands are required. Eg: + 2 4.6
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py + 3 5 7
In essence, an operator and two number operands are required. Eg: + 2 4.6
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py *5 7
In essence, an operator and two number operands are required. Eg: + 2 4.6
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py * 5 7
In essence, an operator and two number operands are required. Eg: + 2 4.6
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py '*' 5 7
35.0
otumian@monkey-tail:~/Projects/Clirithmetic-oe$ python3 app.py \* 5 7
35.0
otumian@monkey-tail:~/Projects/Clirithmetic-oe$
```

## Source

-   [python-doc]
-   [Clirithmetic]

## Conclusion

Clirithmetic performs binary arithmetic operations on the CLI. Data taken from the CLI is parsed then evaluated by the back-end code. There was an instance where we skipped several `if statements` by passing the index of the operator instead of the operator character instead. We raised exceptions instead and passed custom messages to the exception raise rather than relying on the default message. In the sample output, we notice that operations such as `/, %, *, **` needed escaping. We can put then in a quote instead. Clirithmetic was meant to teach how to pass values and make use of these values, from the CLI. An Advanced version of Clirithmetic is where one uses a database as a memory for the calculations. Clirithmetic is limited to binary operations and can be expanded to accept multiple operands. Good luck, hacking and any suggestion or critic is welcome.

##

[python-doc]: https://docs.python.org/3/library/sys.html?highlight=sys#sys.argv
[clirithmetic]: https://github.com/Otumian-empire/Clirithmetic-oe
