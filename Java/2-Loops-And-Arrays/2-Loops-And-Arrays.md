# [Loops and Array](#top)

<div id="top"/>
In this session, we will discuss:

-   [Loops](#loops)
-   [Array](#array)
-   [Conclusion](#conclusion)

## [Loops](#top)

<div id="loop" />

When we discussed Conditions, we learnt that `if-else` statements are ways we can execute some instructions based on the truth value of some conditions. So to know whether a number is an even number, we have to find the remainder of the number when divided by two and check, `if` the remainder if zero. If the remainder is not zero the `else` block of the `if-else` statement is executed.

```java
int number = 5;

if (number % 2 == 0) {
    System.out.println(number + " is even");
} else {
    System.out.println(number + " is not even");
}
```

In the case of a loop, a group of statements is repeated some number of times or as long as some condition holds. We can print `"Hello world"` to the screen using a loop rather than just repeat, `System.out.println(number + " is even")` five times.

```java
// print Hello World five times
System.out.println("Hello world");
System.out.println("Hello world");
System.out.println("Hello world");
System.out.println("Hello world");
System.out.println("Hello world");
```

The whole idea of loops is repetition, but it is to avoid repetition.

In Java, there are three ways to perform repetitions. These are:

-   For Loop
-   While Loop
-   Do-While Loop

### For Loop

The syntax for a `for` loop looks like:

```java
for (initialization; condition; step) {
    // do something here
}
```

-   `initialization`: This is where the loop starts, the initial value for the `looping variable`. This so-called `looping variable` is what we use to keep track of the number of times the content the `condition` held. We could call it a "loop counter" or "start". This part is only executed once.
-   `condition`: This indicates when the loop should end or terminate. The loop terminates when the `condition` evaluates to `false`. We call this `end`.
-   `step`: This is known to increase or decrease the `looping variable`.
-   Note the semicolon after the `initialization` and `condition`.

> Create a class, `ForLoopHello`. Let's print `"Hello world"` to the screen using a loop.

```java
public class ForLoopHello {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            System.out.println("Hello world");
        }
    }
}
```

-   `initialization`: `int i = 0`, we start the loop from `0`, that is, `i` is initialized to `0`.
-   `condition`: `i < 5`, the loop should execute as far as the `looping variable` is less than `5`.
-   `step`: After the body of the `for` loop is executed, _increase_ or _decrease_ the `looping variable`. In this case, increase - add one to the `looping variable`. `i++` is the same as `i = i + 1` and `i+=1`.

If your `ForLoopHello class` looks like the above snippet and there is no error, compiling then executing will print `Hello world` five times to the screen.

For most starters, why didn't we start the loop initialization from `1` but `0`? Change `int i = 0` to `int i = 1` and see the number of times `Hello world` is printed out.

The table below will demonstrate how the `for` loop is working.

| `i` | `i < 5` | `i++` |
| :-: | :-----: | :---: |
|  0  | `true`  |   1   |
|  1  | `true`  |   2   |
|  2  | `true`  |   3   |
|  3  | `true`  |   4   |
|  4  | `true`  |   5   |
|  5  | `false` |       |

> Create a class, `ForLoopFactorial`. The factorial of a number, `x` is `x! = x*(x-1)*(x-2)*(x-3)*...*1`. When `x = 1`, `x! = 1`, and `x = 0`, `x! = 1`. So our loop should execute when `x > 1`.

```java
import java.util.Scanner;

public class ForLoopFactorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        sc.close();

        int factorial = 1;

        if (number > 1) {
            for (int i = 2; i <= number; i++) {
                factorial *= i;
            }
        }

        System.out.println("Factorial of " + number + " is " + factorial);
    }
}
```

### While Loop

A `while` Loop of the form:

```java
while (condition) {
    // do-something
}
```

The `condition` must evaluate to `true` for the body of the while loop to execute (just like the `if` statement and `for` loop).

The `while` loop in most cases can be used in place of a `for` loop.

> Create a class, `WhileLoopEnterExist`, we will continuously print whatever the user enters starting with, `You entered `. The program would terminate and print, `Program ended` when the user input is exactly, `exit`.

```java
import java.util.Scanner;

public class WhileLoopEnterExist {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String userInput = sc.next();

        while (!userInput.equals("exit")) {
            System.out.println("You entered " + userInput);
            userInput = sc.next();
        }

        sc.close();

        System.out.println("Program ended");
    }
}
```

To compare `String` types, we use the `String` _method_ `equals`. Try to see if you could explain what the snippet about is doing. Why was `userInput = sc.next();` pass in the `while` loops body? Why was the `Scanner` object closed outside the `while` loop?

> Create a class, `WhileLoopFactorial`. We shall rewrite the `ForLoopFactorial` using a while loop.

```java
import java.util.Scanner;

public class WhileLoopFactorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        sc.close();

        int factorial = 1;

        if (number > 1) {
            int i = 2;

            while (i <= number) {
                factorial *= i;
                i++;
            }
        }

        System.out.println("Factorial of " + number + " is " + factorial);
    }
}
```

Open `WhileLoopFactorial` and `ForLoopFactorial` side by side and compare the snippets.

Give a `for` loop for the form:

```java
for (initialization; condition; step) {
    // do something
}
```

We could rewrite this using a `while` loop as :

```java
initialization;

while (condition) {
    // do something
    step;
}
```

### Do-While Loop

A `do-while` loop is like a `while` just that a `do-while` loop may be executed once.

It has the syntax:

```java
// may be initialization
do{
    // something
    // maybe step
} while(condition);
```

> Create a class, `DoWhileLoopFactorial`. We would rewrite the `WhileLoopFactorial` using a `do-while` loop.

```java
import java.util.Scanner;

public class DoWhileLoopFactorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        sc.close();

        int factorial = 1;

        if (number > 1) {
            int i = 2;

            do {
                factorial *= i;
                i++;
            } while (i <= number);
        }

        System.out.println("Factorial of " + number + " is " + factorial);
    }
}

```

### When Should We Use Which Loop

-   Use a `for` loop when you are certain of the number of times to loop
-   Use `while` loop when the termination of the loop is based on a condition
-   Use the `do-while` loop when you expect the code to run once
-   Use any of them when you feel like, how you feel like, there is no restriction
-   use what is best for you

## [Array](#top)

<div id="array" />

Let's start with a problem.

> Write a program that prints the sum and average of the five integers.

This simple, all we have to do is initialize seven variables. Five for the numbers, one for the sum and the last for the average. You would then have to do something like:

```java
int num1 = 3;
int num2 = 2;
int num3 = 1;
int num4 = 5;
int num5 = 4;

int numSum = num1 + num2 + num3 + num4 + num5;

int numAvg = numSum / 5;

System.out.println("Sum: " + numSum);
System.out.println("Average: " + numAvg);
```

What would you do if the number of scores is about thirty or above? The above approach will not be helpful and worse, would when we are taking input.

An array is best suitable for things like this.

An array is a collection of data of the same type. So we can have an array of `int`, `String`, etc. With an array, we won't have to initialize several variables.

As we could declare an `int` variable, `int num;`, we could declare an array as `int[] nums;`. The `[]` after the _type_ indicates it is an array.

An array holds a collection of data as such we have to pass the size (number) of the collection. This will be in the form, `type[] var_name = new type[size];`. For the problem above we'd do, `int[] nums = new int[5];`.

Arrays as we know is a collection of data, but contiguous data. So `int[] nums = new int[5];` will have five different element. Each element of the collection has a position known as the index. The first index of the collection is `0`, then `1`, and so on. This is what we meant by contiguous.

To assign and read an element from an array, we use the index (position) of the element. For the first element, we can do, `nums[0] = 3;`. The second, `nums[2] = 2;` and so on. At times, we say that the `index = position - 1`. So the first positioned element will be at index, `0`. The last positioned element will be at index, `5 - 1`.

The above snippet will look like this:

```java
int[] nums = new int[5];

nums[0] = 3;
nums[1] = 2;
nums[2] = 1;
nums[3] = 5;
nums[4] = 4;

int numSum = nums[0] + nums[1] + nums[2] + nums[3] + nums[4];

int numAvg = numSum / 5;

System.out.println("Sum: " + numSum);
System.out.println("Average: " + numAvg);
```

Both snippets are almost the same just that in the first we are using variables but here we are using an array.

There is another approach for creating an array that looks simple. Instead of doing `new type[size]` would do `{val1, val2, ..., valN}` where the _size_ of the array is `N`. An array of five integers would look like, `int[] nums = {3, 2, 1, 5, 4};`. The elements are comma-separated and each position corresponds to the index of the element in the array.

The above snippet could written as:

```java
int [] nums = {3, 2, 1, 5, 4};

int numSum = nums[0] + nums[1] + nums[2] + nums[3] + nums[4];

int numAvg = numSum / 5;

System.out.println("Sum: " + numSum);
System.out.println("Average: " + numAvg);
```

The number of lines has decreased. What do you think will happen, if we have to deal with about fifty sized array? Will we be doing `nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + ... + nums[49]` ?😥️

We can loop through the array using any of the loops. We will use a `for` loop to print out the content of the array.

```java
int [] nums = {3, 2, 1, 5, 4};

for (int index = 0; index < 5; index++) {
    System.out.println("Element at index: " + index + " is " + nums[index]);
}
```

> Let's create a class, `ArrayLoopAverage`. We will use the `for` loop here.

```java
import java.util.Scanner;

public class ArrayLoopAverage {
    public static void main(String[] args) {
        int[] nums = new int[5];
        Scanner sc = new Scanner(System.in);

        // prompt user for the five scores
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter " + (i + 1) + "th score: ");
            nums[i] = sc.nextInt();
        }

        sc.close();

        int numSum = 0;

        for (int i = 0; i < 5; i++) {
            numSum += nums[i];
        }

        int numAvg = numSum / 5;

        System.out.println("Sum: " + numSum);
        System.out.println("Average: " + numAvg);
    }
}
```

We could do the above without an array.

> Let's create a class, `LoopingAverage`. We will make use of just one variable. I want you to see how the code would change so I will comment out those that will not be needed.

```java
import java.util.Scanner;

public class LoopingAverage {
    public static void main(String[] args) {
        // int[] nums = new int[5];
        int numSum = 0;

        Scanner sc = new Scanner(System.in);

        // prompt user for the five scores
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter " + (i + 1) + "th score: ");
            // nums[i] = sc.nextInt();
            numSum += sc.nextInt();
        }

        sc.close();

        // int numSum = 0; // moved to the top

        // for (int i = 0; i < 5; i++) {
        // numSum += nums[i];
        // }

        // int numAvg = numSum / 5;

        System.out.println("Sum: " + numSum);
        System.out.println("Average: " + (numSum / 5));
    }
}
```

<div id="conclusion" />

## Conclusion

A loop saves us from writing a lot of lines. Know when to use a loop. Whenever you use an array, review your code to see if a single variable could be used. Avoid nesting as much as you can, this is not a restriction. There is another simple way for writing a `for` loop but we didn't discuss it. I believe an example we do:

```java
int[] nums = {1,2,3,4,5};
int numSum = 0;

for (int num : nums) {
    numSum += num;
}

System.out.println("Sum: " + numSum);
```

`for (int num: nums)` can be read as _for each number in numbers_ from the first to the last index.

We could also `break` out of a loop using the `break` keyword.

### Projects

-   Write a program that reads a student's name followed by five test scores. The program should output the student name, the five test scores, and the average test score. Display the name on the first line, the scores on the same line on the second line and the third line, the average. (Use a loop)

-   Write a program that reads a set of integers and then finds and prints the sum of the even and odd integers, separately.

-   Write a program to find the factorial of even numbers from 3 to 12 inclusive.

-   Write a program that declares an integer array `numbers` of 25 elements. Initialize the array so that the first 15 elements are equal to the square of the index variable, and the rest are equal to three times the index variable. Output the array so that five elements per line are printed.

### Source

-   Sololearn
-   DS Malik

<a href="#top">Top</a>
