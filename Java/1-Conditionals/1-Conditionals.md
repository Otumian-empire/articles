# [Conditionals](#top)

<div id="top"/>
In this session, we will discuss:

-   [If Statement](#if-statement)
-   [Comparison Operators](#comparison-ops)
-   [If-Else Statement](#if-else)
-   [Nested If Statements and If-Else-If Statement](#nested-if-else)
-   [Logical Operators](#logical-ops)
-   [Conclusion and Programming Projects](#conclusion)

Assume the IT Department of the Highway Patrol Team contacted you to write a program that alerts them when a vehicle speeds at `100km/h` on the highway. They have given you all the information and models you would need to write the program. Now, how would you know if a vehicle is speeding at or exceeding the speed limit set by the HPT?

A decision has to be made. I don't think it will be great and legal to flag a vehicle at `70km/h`, would it? So before the alert is sent, we have to know if the vehicle's speed exceeds the said limit. Decision making is the whole idea of `if` statements in programming.

## [If Statement](#top)

<div id="if-statement" />

An `if` statement allows us to perform certain actions based on the truth value of some process (condition). These truth values are `true` and `false` (Refer to `boolean` types).

An `if` statement is of the form:

```java
if (condition) {
    //
}
```

> Let's create a class, `IfBoolean`.

In this class, we will pass `true` into the `if` statement and print `"This is true"`. On the next line after closing curly braces, instead of `true`, we'd pass `false` into an `if` statement and we'd print `"This is false"`. This activity is for us to know that the `if` block is only executed when the condition evaluates to `true`.

```java
public class IfBoolean {

    public static void main(String[] args) {
        if (true) {
            System.out.println("This is true");
        }

        if (false) {
            System.out.println("This is true");
        }
    }
}
```

Only `"This is true"` was printed on the screen. If you were to be using vscode with the java extension, `Extension Pack for Java (vscjava.vscode-java-pack)`, you would see that the second if statement would be called a `Dead code`. This means it is not useful since the body of that `if` statement will never be reached.

## [Comparison Operators](#top)

<div id="comparison-ops" />

Conditions passed to the `if` statement is always evaluated to a `boolean`. We don't have to be passing the value to it all the time instead, we can compare the value of interest to some fixed or constant value. This will evaluate to a `boolean`.

> Comparison operators are binary operators.

| Operator | Name                     | Examples          |
| -------- | ------------------------ | ----------------- |
| `<`      | Less than                | `1 < 2 => true`   |
| `>`      | Greater than             | `1 > 2 => false`  |
| `==`     | Equal to                 | `1 == 2 => false` |
| `<=`     | Less than or equal to    | `1 <= 2 => true`  |
| `>=`     | Greater than or equal to | `1 >= 2 => false` |
| `!=`     | Not equal to             | `1 != 2 => true`  |

`==`, the double `equal to sign` is used for comparing two values if they are the same. The opposite of `==` is `!=`, read as `not equal to`. `=`, the single `equal to sign` is called the assignment operator. It is used in the declaration and initialization of variables.

> Let's create a class, `IfCompare`

We will compare the user's speed limit to the Highway Patrol Team's value they gave us which was `100km/h`.

```java
public class IfCompare {

    public static void main(String[] args) {
        int HIGHWAY_SPEED_LIMIT = 100;

        int vehicle_speed = 75;

        if (vehicle_speed >= HIGHWAY_SPEED_LIMIT) {
            System.out.println("Alert: HPT, we have a speedster");
        }
    }
}
```

> You should try your hands on the other comparison operators.

## [If-Else Statement](#top)

<div id="if-else" />

Let's reconsider the `IfCompare` class. What do you think we should have done when the vehicle's speed was within the speed limit? Well, nothing. If the vehicle is within the speed limit can not call the HPT on them. Maybe we could buy them pizza at the next drive-through or compliment them. To do compliment them we can pass the `else` body after the `if` statement's body to do just that.

> Create a class, `IfElseParity`

We will write a program that takes a user input as assigns it to an `int` variable, `userInput`. Check if the user input is even then print `"<userInput> is Even"` else print, `"<userInput> is Odd"`. where `<userInput>` is the `userInput`. (Make use of `%` operator)

```java
import java.util.Scanner;

public class IfElseParity {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int userInput = scanner.nextInt();

        scanner.close();

        if (userInput % 2 == 0) {
            System.out.println(userInput + " is Even");
        } else {
            System.out.println(userInput + " is Odd");
        }
    }
}
```

## [Nested If Statements and If-Else-If Statement](#top)

<div id="nested-if-else" />

We know about the `if-else` statement. We can have `if` statements nested in each other. It will look like this:

```java
if (condition1) {
    // if condition1 holds
    if (condition2) {
        // if condition2 holds do something
    } else {
        // do something if condition2 doesn't hold
    }
} else {
    // do something if condition1 doesn't hold
}
```

There are instances where the nested `if` statement is useful and there at moments they don't shine. They obscure the logic and makes it hard to read, for (some) humans. We can use the `if..else-if..else` approach. This will look more like this:

```java
if (condition1) {
    // do task 1
} else if (condition2) {
    // do task 2
} else {
    // do some other task
}
```

Let's solve a modified version of the `FizzBuzz` problem.

> The `FizzBuzz` program: Given a list (array) of numbers, check if an element is divisible by three and print `Fizz`, check if the number is divisible by five and print `Buzz`. If the number is both divisible by three and five (line 15, 30), print `FizzBuzz` else print the number.

> For our modified version, we just take the input and apply the concept rather. We will use the nested and `if..else-if..else` approach.

> Create a class, `FizzBuzzNested`.

```java
import java.util.Scanner;

public class FizzBuzzNested {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int userInput = scanner.nextInt();

        scanner.close();

        if (userInput % 3 == 0) {
            if (userInput % 5 == 0) {
                System.out.println("FizzBuzz");
            } else {
                System.out.println("Fizz");
            }
        } else {
            if (userInput % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(userInput);
            }
        }
    }
}
```

Try this with several inputs like: `2, 3, 5, 9, 10, 15`

Now for the other approach, let' create a class, `FizzBuzzIfElseIfElse`

```java
import java.util.Scanner;

public class FizzBuzzIfElseIfElse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int userInput = scanner.nextInt();

        scanner.close();

        // check if it is divisible by 3 and 5
        if (userInput % 3 == 0) {
            if (userInput % 5 == 0) {
                System.out.println("FizzBuzz");
            } else {
                System.out.println("Fizz");
            }
        } else if (userInput % 5 == 0) {
            System.out.println("Buzz");
        } else {
            System.out.println(userInput);
        }

    }
}
```

This looks a little different but it is better on our eye. We did run into some issues. Maybe you asked yourself, "how do I check if `userInput` is divisible by both three and five?" Let's discuss that.

## [Logical Operators](#top)

<div id="logical-ops" />

So far we have done Arithmetic and Comparison (Relational) Operators. For the Logical Operators, they are used to combine comparison expressions to form a compound expression.

These are `AND` represented as `&&` and `OR` represented as `||`. These are also binary operators.

For `AND`, both sides must evaluate to `true` before the whole expression becomes `true`. If one of the two expressions is `false`, the whole will be `false`.

| Operand A | Operand B | Result  |
| :-------: | :-------: | :-----: |
|  `true`   |  `true`   | `true`  |
|  `true`   |  `false`  | `false` |
|  `false`  |  `true`   | `false` |
|  `false`  |  `false`  | `false` |

In a code:

```java
if (condition1 && condition2) {
    // do something
}
```

For `OR`, both sides must be `false` before the whole expression becomes `false`. If at least, one, of the two expressions is `true`, the whole becomes `true`.

| Operand A | Operand B | Result  |
| :-------: | :-------: | :-----: |
|  `true`   |  `true`   | `true`  |
|  `true`   |  `false`  | `true`  |
|  `false`  |  `true`   | `true`  |
|  `false`  |  `false`  | `false` |

In a code:

```java
if (condition1 || condition2) {
    // do something
}
```

It is time to tackle the issue we had in the `FizzBuzzIfElseIfElse` class.

> Create a class, `FizzBuzzLogical`.

We will make use of the logical operators instead of nesting.

```java
import java.util.Scanner;

public class FizzBuzzLogical {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int userInput = scanner.nextInt();

        scanner.close();

        if (userInput % 3 == 0 && userInput % 5 == 0) {
            System.out.println("FizzBuzz");
        } else if (userInput % 3 == 0) {
            System.out.println("Fizz");
        } else if (userInput % 5 == 0) {
            System.out.println("Buzz");
        } else {
            System.out.println(userInput);
        }

    }
}
```

## [Conclusion](#top)

We discussed `if` and `if..else` statements. The body of the `if` statement executes when the condition revaluates to `true` else the `else` block is executed. We can nest if statement but using `if..else-if..else` construct is better. It makes the code readable. We can use the Logical `&&` and `||` to form compound expressions. This can reduce the number of different blocks of code we have.

### Projects

-   Write a program that prompts the user to input a number. The program should then output the number and a message saying whether the number is positive, negative, or zero.
-   Write a program that prompts the user to input three numbers. Sorts and prints the three numbers in ascending order.
-   One way to determine how healthy a person is, is by measuring the body fat of the person. The formulas to determine the body fat for females and males are as follows:

    -   Body fat formula for women:

        ```
        A1 = (Body weight x 0.732) + 8.987
        A2 = Wrist measurement (at fullest point) / 3.140
        A3 = Waist measurement (at navel) x 0.157
        A4 = Hip measurement (at fullest point) x 0.249
        A5 = Forearm measurement (at fullest point) x 0.434
        B  = A1 + A2 – A3 – A4 + A5
        Body fat = body weight – B
        Body fat percentage = body fat x 100 / body weight
        ```

    -   Body fat formula for men:
        ```
        A1 = (Body weight x 1.082) + 94.42
        A2 = Waist measurement x 4.15
        B = A1 – A2
        Body fat = body weight – B
        Body fat percentage = body fat x 100 / body weight
        ```

    Write a program to calculate the body fat of a person.

### Source

-   Sololearn
-   DS Malik

<a href="#top">Top</a>
