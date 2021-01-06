# Arithmatic on the Commandline - Clirithmatic

## Introduction

Adding numbers is one thing but doing it on the commandline is another. Clirithmatic combines the CLI as the front-end and python as the back-end to perform binary arithmatic operations such as addition, subtraction, division, multiplication, modulo and exponents. We shall separate the back-end from the front-end so to make our code managable and easy to maintain.

## Content

### The Back-end

The Back-end as the front-end is quite simple to implement. With some knowledge of python, this would be easy to read and comprehend. Let's create a file called `backend.py` for our backend code. It would be easier if we use functions but we better a class.

```python
# backend.py
class Backend:

    def __init__(self, operator, operand1, operand2):
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2
```

In the code above, is a class in the `backend.py` file called `Backend` with a constructor that accepts the operator and the two operands.

```python
# backend.py
class Backend:

    ...

    def add(self):
        return self.self.operand1 + self.operand2

    def mult(self):
        return self.self.operand1 * self.operand2

    def subt(self):
        return self.self.operand1 - self.operand2

    def div(self):
        return self.self.operand1 / self.operand2

    def mod(self):
        return self.self.operand1 % self.operand2

    def exp(self):
        return self.self.operand1 ** self.operand2
```

The code above defines methods (functionalities for the class) to perform the arithmatic operations. It is obvious that these function can be read easily and understood but what problems are we getting into?

How are we going to know which method to call based operation passed? We know the function to call based on the operator. How are we going to do that? Let's say we needed a parser - this parser's job is to break the input we shall take from the CLI into the operator and the two operands. Also, we would use this same parser to catch any wrong data that is passed. We need only the operator to be a string and the operands as integer or float.

**We are accepting three inputs:**

- the first the operator,
- then the first and second operands, respectively.

We can debate on whether to add the parser as a methid to the `Arithmatic class` or make it a stand alone function. It is easier without tweaking, to make the parser a function than a method of the class. I think it can be done. What do you think?

```python
# parser.py
# data from the CLI is a list - params
# the parser shall also return a list if the parsing
# was successful else raise an error and exit with an
# error message

# destructure param
# operator, first operand, second operand = param
def parser(params):
    try:
        pass
    except:
        pass



```

<!-- Source -->
<!-- Conclusion+question -->
