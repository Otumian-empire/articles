# [Java Tutorial](#top)

<div id="top"/>

In this session, we will discuss:

-   [Hello World Program In Java](#hello)
-   [Comments](#comment)
-   [Variables and Types and Primitive Operators](#var-ops)
-   [Strings Datatype](#string)
-   [Get User Input](#input)
-   [Conclusion and Programming Projects](#conclusion)

<div id="hello"/>

## Hello World Program In Java

In any introductory programming class, if it is language-based, we write the "Hello world" program. This program just outputs "Hello world" to the console/screen when the program is executed/run. In java, this snippet below is the "Hello world" program.

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello world");
    }
}
```

To create a "Hello world" program, create a file in your project directory called, `HelloWorld.java` then copy and paste the above snippet and save the file.

### Can A Different File Name Be Used?

Yes, a different file can be used. You can choose `Main.java`, `Hello.java`, etc. Make sure that the file name matches that of the `class` name. For our "Hello world" program with the file name, `HelloWorld.java` the `class` name is on the line, `public class HelloWorld {`. For a file with the name, `Main.java`, the `class` name line will be `public class Main {`. Just make sure the `class` name matches the file name.

### Compile

We need the java compiler, `javac`, to compile the `.jav` file to a `.class` file. Run `javac HelloWorld.java` in the terminal where the `HelloWorld.java` is. On a successful compilation, `HelloWorld.class` will be created. Run `java HelloWorld` to execute the `HelloWorld.class`. If there was no error then you should see, `Hello world` on the terminal.

> The `.class` file is called a byte code. Try and read what a byte code is, in Java.

### Hello World Break Down

Now, there are a few things that one has to understand when it comes to java.

-   Java is a compiled language, which produces a byte code that can run on any machine. (Java is machine Independent)
-   Java is Object Oriented (We use class for everything)
-   It is a conversion that a java file should have the same name as its class name.
-   A java program (the class) must have a main method (function)
-   The main method is always, `public static void`.
    -   `public`: accessible outside the class or file
    -   `static`: to use the main method, we don't have to create an instance of the class
    -   `void`: the function returns nothing or doesn't return a value
    -   `main(String[] args)`: the main method takes an array of strings as an argument, called `args`. So you can change `args` to `values` and it will still work.
    -   `System.out.println("Hello world");`: displays `Hello world` to the screen.
-   Java is block-based. The block of a class or function begins with `{` and ends with `}`. Whatever goes with the `{ }` is the block/body of that contract.

<div id="comment"/>

## Comments

A comment is the part of the code that the compiler ignores. We add a comment to our code :

-   to explain what the code is doing
-   to explain why we choose one approach over another
-   to document our code

Java has two ways of commenting. The single line and multiline commenting. The multiline is also known as a block comment.

We use two forward slashes, `//`, without any space or character between them, at the beginning of a line of code to comment that line out. The compiler will skip that line during compilation.

We use `/*` and `*/` to block/bulk/multiline comment. Whatever ever is found within `/*` and `*/` will be commented and skipped during compilation.

> create a java class `Comment` (The file name will be `Comment.java` and will have a class name `Comment`)

Enter the Snippet below, compile and execute it and see which lines are printed and those that aren't. Comment out the last line of code and later the whole code in the main method's block.

```java
public class Comment {
    public static void main(String[] args) {

        // System.out.println("Line 1");
        System.out.println("Line 2");
        System.out.println("Line 3");
        /*
         * System.out.println("Line 4");
         * System.out.println("Line 5");
         */

        // single line comment
        /* multiline comments */
        /**
         * Java doc
         * This is a java documentation
         */
    }
}
```

<div id="var-ops"/>

## Variables and Types and Primitive Operators

Variables act as a storage medium for data/values that we use in our code. A variable is a name/placeholder/tag that points to the value/data saved in memory. Without a variable, we would have to personally and mentally keep track of values we use in our code, when we used them, against what other values and operators, and how they have changed. A variable stores data of the same type. What then is a type?

### Types

The kind of data we use in our program is called the data type. This type can be a `String`, `char`, `int`, `float`, `double`, `boolean`, etc. These types here a fundamental. `void` is a type, but it is nothing. `float` and `double` are the same but `double` has more memory (space) as such can store more huge values compared to `float`. We'd stick to `double` here.

> Remember that the type of a variable corresponds to the type of data assigned (stored)

Here are some examples of data types we can use.

-   `double`: This is like a real or decimal number, the measurable values like weight, speed, etc. Example: `1.34, 3.456, -23.002`
-   `int`: This is an integer, the countable values like, the number of humans, the number of books. Example: `1, 2, 3, -4, 400`
-   `char`: This is a single character enclosed in single-quotes . Example: `'A', 'a', '+', '10', '0', '\n'`. A typical example is a student grade.
-   `String`: This a sequence of characters enclosed in double-quotes, `"..."`. Example:`"animal", "peter", "Java", "1234", "30'C", ""`
-   `boolean`: This has two possible value, `true` or `false`.

### Variable Declaration and Initialization

Now we know what variables are and what types are. To create a variable, we need the type of the variable (which will be the same as that of the value), a placeholder/name, assignment operator and the value, followed by a semi-colon. Just like this: `type name = value;`.

> Let's create a class called `Variable`.

We will initialize a variable called

-   `age` of type, `int` and assign it a value of `30`
-   `fullName` of type `String` and assign it a value of `" John Doe"`
-   `grade` of type `char` and assign it a value of `'A'`
-   `isProgrammer` of `boolean` and assign it a value of `true`
-   `weight` of type `double` and assign it a value of `57.6`

```java
public class Variable {
    public static void main(String[] args) {
        int age = 30;
        String fullName = "John Doe";
        char grade = 'A';
        boolean isProgrammer = true;
        double weight = 57.6;

        System.out.println("My name is " + fullName);
        System.out.println("I am " + age + " years old");
        System.out.println("It is " + isProgrammer + " that I am a programmer");
        System.out.println("I want grade " + grade + " this semester");
        System.out.println("Now I weight, " + weight + "kg because of programming");
    }
}


```

All that we have done so far is variable initialization. How do we then declare a variable?

Simple! We do, `int age = 30;` to initialize `age` by assigning it a value of `30`, to declare age, we would do, `int age;` then later in our code, we'd assign it a value.

> Every line that is not part of a contract must end in a semicolon. Look into the snippets so far to see where semicolon was used and where it wasn't to be sure.

### Operators

We can do math in java, using:

-   `plus -> +`
-   `minus (subtraction) -> -`
-   `division -> /`
-   `multiplication -> *`
-   `remainder (modulo) -> %`

It is obvious what these operators are so let's see how to use them.

```java
public class Operators {

    public static void main(String[] args) {

        // initialized two integer variables
        int johnsAge = 32;
        int hannahsAge = 28;

        // plus
        int sumOfTheirAges = johnsAge + hannahsAge;

        // minus
        int differenceInTheirAges = johnsAge - hannahsAge;

        // multiplication
        int johnsAgeTime5 = johnsAge * 5;

    }
}
```

> Complete the above snippet for other operators and add a nice output for each operation.

<div id="string"/>

## String Datatype

We know that `String`s are double-quoted. We saw `System.out.println("My name is " + fullName);` in one of the snippets above. Using the `+` operator to combine `String` type values with other type values is feasible in java. `String` + `another_type` will be a `String`. This is called String concatenation.

<div id="input"/>

## Get User Input

So far we have injected data directly into our code. Let's look at how we can take one from the user. In java, the most common way of taking data from the user is through the `Scanner` object. We would have to import `Scanner` by typing at the very top of our code, `import java.util.Scanner;`

> Note the semicolon at the end

> Create a `class` called `Input`

We shall create an instance of the `Scanner` `class`.

```java
import java.util.Scanner;

public class Input {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(scanner.next());

    }
}

```

`Scanner scanner = new Scanner(System.in);` We created a `Scanner` object called `scanner`. The `new` indicates that `scanner` is a `new` instance of the `Scanner` class. `scanner` can be replaced with any variable name.

Compare `Scanner scanner = new Scanner(System.in);` to `int age = 34;`, are there some similarities?

-   types: `int`-> `Scanner`,
-   variables: `age` -> `scanner`
-   value: `34` -> `new Scanner(System.in)`

`new Scanner()` here takes input, when we pass `System.in`, we are then instructing `new Scanner` to accept input from the standard input, which is the keyboard.

`scanner.next()` takes the first of whatever you type into the terminal before a white space and `System.out.println(scanner.next());` displays it to the screen.

Run the snippet above several times with several different inputs to see how `scanner.next()` behaves.

We learnt that `double`, `int`, `float` and `char` are all types but by default, all inputs are `Strings`. You have to convert it to the desired type as you wish.

To do that we have:

-   `next()`: reads in a word, a `String`. (a sentence is a space-separated words - the first word is taken as input after one hits `enter`)
-   `nextLine()`: reads a whole line (sentence), a `String`. So use this when you want a sentence from the user.
-   `nextInt()`: Reads in the data as an `int`
-   `nextDouble()`: Reads in the data as an `double`

> Create `InputWithVariable` class

We will rewrite one of the snippets above, but this time we'd use variables to hold the data, taken from the keyboard.

```java
import java.util.Scanner;

public class InputWithVariable {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // read in a line - fullName is separated by space
        System.out.print("Enter full name: ");
        String fullName = input.nextLine();

        // read in an integer value and assign it to age
        System.out.print("Enter age: ");
        int age = input.nextInt();

        // read in a character using the next()
        // because grade is of type char, it will take just the
        // first character from word with `.charAt(0)`
        System.out.print("Enter grade: ");
        char grade = input.next().charAt(0);

        // get boolean input, true/false
        System.out.print("Are you a programmer, enter: true|false: ");
        boolean isProgrammer = input.nextBoolean();

        // get a double just like int
        System.out.print("Enter weight: ");
        double weight = input.nextDouble();

        // close the scanner object
        input.close();

        // System.out.println() prints out a newline character after
        // its arguments
        System.out.println();
        System.out.println();

        System.out.println("My name is " + fullName);
        System.out.println("I am " + age + " years old");
        System.out.println("It is " + isProgrammer + " that I am a programmer");
        System.out.println("I want grade " + grade + " this semester");
        System.out.println("Now I weight, " + weight + "kg because of programming");
    }
}

```

`System.out.print("Enter weight: ");` is just like `System.out.println("Enter weight: ");` but doesn't add a new line character at the end.

We have to close the `Scanner` object when we open (initialize) it else there will be memory leaks (you could get a warning).

<div id="conclusion" />

## Conclusion

We discussed `Hello World Java`, Comments, Variables and Data types and some operators for arithmetic. We look at how to take input from the user and parse it to the desired type. This is enough to get our paws dirty a bit.

### Projects

-   Write the program that takes as input three numbers and print the sum of the first two numbers multiplied by the third number to the screen. (Assume that the three numbers are of type double.)

-   Write a program that prompts the user to enter the weight of a person in kilograms and outputs the equivalent weight in pounds. Output both the weights, saying, `X weights is Y Pounds`. (Note that 1 kilogram = 2.2 pounds.)

-   Write a program that reads a student's name followed by five test scores. The program should output the student name, the five test scores, and the average test score. Display the name on the first line, scores on the same line on the second line then on the third line the average.

### Source

-   Sololearn
-   DS Malik

<a href="#top">Top</a>
