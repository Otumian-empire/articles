# [Class and Method](#top)

<div id="top"/>
In this session, we will discuss:

-   [Class](#class)
-   [Access modifiers](#access_modifiers)
-   [What is a method?](#methods)
-   [static methods](#static_methods)
-   [Class instance](#class_instance)
-   [String methods](#string_methods)
-   [Array methods](#array_methods)
-   [Math class](#math_class)
-   [Conclusion](#conclusion)

## [Class](#top)

<div id="class" />

We have created a lot of classes up to now. Java is an **Object Oriented Programming language**. Java uses classes. We create a java `class` then we create an instance of the said java `class`. This is known as an instantiation or creating an instance of the `class`. This is an instance of the `class` being called an object of the `class` - they are both the same.

So what then is a class?

A `class` is a framework for defining the structure of an object. Class acts as a "blueprint" for an object, dictating what qualities and behaviour of an object. These qualities are sometimes called fields, attributes or properties. These qualities keep track of the state of the object (by state, I meant data). The behaviour of an object is basically a method.

We already know we can define a `class` by doing:

```java
class HeroClass {

}
```

We used the `class` keyword followed by the `class` name, _HeroClass_ to define a class.

## [Access modifiers](#top)

<div id="access_modifiers" />

An access modifier is used to regulate the level of accessibility (reading and writing) of a `class`. If another object can access our `class`, methods or attributes, should we allow the object to change the state or behaviour of our `class` or should the object read the states and call the methods? Obviously, it depends. An access modifier can be applied to a `class`, method or attribute.

For a class, the available access modifiers are `public` and `default`. `default` means, we pass no access modifier.

-   A `default` `class` is only accessible only by classes in the same package (a folder that groups similar classes).
-   A `public` `class` is accessible by any other class.

For a `class` or an attribute, the available access modifiers are `default`, `public`, `protected` and `private`.

-   `default`: accessible by classes in the same package.
-   `public`: accessible from any `class`.
-   `protected`: acts like the `default` but allow accessibility to classes that extend (inherit) the said `class`.
-   `private`: accessible in the declared `class` only.

> Let's create a `public` `class`, `Pet`. With `public` attributes, `name` and `favFood`, with a `public` `void` method, `print` which prints out the name and favourite food of the pet.

```java
public class Pet {
    public String name;
    public String favFood;

    public void print() {
        System.out.println("Name: " + name);
        System.out.println("Favorite Food: " + favFood);
    }
}
```

It looks simple right? The `name` and `favFood` in the `print` method are the same above (outside the `print` method). Currently, the `Pet` class can just compile but nothing else can be done. Their sole purpose here is to observe how the access modifiers are used.

## [What is a method?](#top)

<div id="methods" />

A method is a function. For someone from another language like `c++`, `c`, `python` or `javascript`, the idea that a function is a method is quite simple to understand. If java is your first language, do not worry.

Do you remember the `main` from the classes we have created so far?. All the classes we have created so far have `public static void main(String[] args)`. This `main` is a method. The `print` method in the `Pet` class above is also a method. The `main` method serves as the "main" entry point of our program. A method does something. One of the sources defined a method as a collection of statements grouped to operate. The `print` method prints the `name` and `favFood` of the `Pet` `class`.

> Let's create a class, `Main` with the `main` method.

```java
public class Main {

    public static void main(String[] args) {

    }
}
```

## [static methods](#top)

<div id="static_methods" />

The `main` method we have is a `static` method. `public static void main(String[] args)`, has the `static` keyword after the access modifier and before the return type, `void`.

When a `field` or `method` is made `static`, we don't have to create an instance of its `class` to use it. We just use the class name, dot the method or attribute name.

> In the `Pet` `class` let's add a new `public` `int` field, `counter` initialized to `0`. We will use it to keep track of the number of times the `print` was called. We will also add a new `public` `static` method `cute`, that prints, `"Pet is cute"`.

> When a return type of a method is not given, use `void`. Try to guess the type of an attribute based on the name or what it will be used for. This also applies to a method.

```java
public class Pet {
    public String name;
    public String favFood;
    public static int counter = 0;

    public void print() {
        System.out.println("Name: " + name);
        System.out.println("Favorite Food: " + favFood);
        counter++;
    }

    public static void cute() {
        System.out.println("Pet is cute");
    }
}
```

The new `Pet` class would look like the above.

_It will be best to create a separate class for any other class we will be creating from here onwards. Create an instance in another class that has the main method._

## [Class instance](#top)

<div id="class_instance" />

The `Pet` `class` has no main method. If it has a main method, we won't be able to call `print` in main. So what we will do is we will create an instance of the `Pet` `class` in the `Main` `class` instead. Since the `Main` and `Pet` `class` are in the same folder, and the `Pet` `class` is `public`, we can directly access it in the `Main` `class`.

Do you remember the `Scanner` `class`? When we want to take an input from the user we create an instance of the `Scanner` `class` then we call its `nextX()` method to read data of type, `X`.

To create an instance of a class, we will do something like, `ClassName instanceVariable = new ClassName();`. This is similar to, `Scanner sc = new Scanner(System.in);` `Scanner` takes a source as argument.

Our `Pet` `class` instance, `Pet bobby = new Pet();`.

> Let's update the `Main` class, in the `main` method, let's create an instance of the `Pet` class. (You can create as many as possible). We will then the necessary fields and call the various methods.

```java
public class Main {
    public static void main(String[] args) {
        Pet bobby = new Pet();

        // We set the fields directly using the Pet instance
        bobby.name = "Bobby Peto";
        bobby.favFood = "Chicken and Salad cream";

        // call the print method
        bobby.print();

        // call the static method
        Pet.cute();

        // update the fields and call print
        bobby.name = "Bobby Pet";
        bobby.favFood = "Chicken, Broccoli and Salad cream";

        bobby.print();

        // call the static field
        System.out.println("the print method was called, " + Pet.counter + " times.");
    }
}
```

These are some of the few things I did and below were the output.

```
Name: Bobby Peto
Favourite Food: Chicken and Salad cream
Pet is cute
Name: Bobby Pet
Favourite Food: Chicken, Broccoli and Salad cream
the print method was called 2 times.
```

The static variable keeps changing the number of times the `print` was called.

## [String methods](#top)

<div id="string_methods" />

Talking about methods, `String` objects also have methods. Check the reference section to be redirected to the source. There are several of them but I shall make mention of those that are or would be used frequently.

-   `charAt(int index)`: returns the element (character) at the said _index_ of the `String` object.
-   `contact(String str)`: joins/adds two strings and returns a new `String`.
-   `contains(String str)`: checks if `String` contains some sequence of `String` and return a `boolean`.
-   `endsWith(String str)`: checks if a `String` ends with some sequence of `String` and returns a `boolean`
-   `equals(String str)`: use this method to check if two strings are the same instead of `==`.
-   `indexOf(String str)`: returns the index of the first occurrence of a `String` else it returns `-1`. We can pass `String` or `char`. We can also pass an of an offset as the second argument which indicates where the search should start from. `indexOf(String str, int offset)`
-   `isEmpty()`: checks if a `String` is empty, the size is greater than `0`.
-   `lastIndexOf(String str)`: returns the last index of a `String` sequence.
-   `length()`: returns the size of a `String`
-   `replace(String str1, String str2)`: replace `str1` with `str2` from the `String`
-   `split(String str)`: split the `String` into an array at `str`
-   `startsWith(String str)`: checks if a `String` starts with some sequence of `String` and returns a `boolean`
-   `substring(int start)`: returns a new `String` starting from `start` index to the end of the `String`. We can pass a second argument for where the substring ends. `substring(int start, int end)`
-   `toLowerCase() and toUpperCase()`: returns a new `String` of the said case respectively.
-   `trim()`: strips the `String` of white spaces - `space, newline, ...`

```java
public class StringMethods {
    public static void main(String[] args) {
        String str = "This is a string";

        // charAt - get the first element
        char firstCharacter = str.charAt(0);
        System.out.println("The first character is: " + firstCharacter);

        // concat
        String newStr = str.concat(", so Hello.");
        System.out.println(str); // this is the original string
        System.out.println(newStr); // this is the new string

        // concat is the same as str1 + str2
        String str1 = "Hello";
        String str2 = "World";
        String str3 = str1 + " " + str2;
        System.out.println(str3);

        // contains
        boolean hasWordString = str.contains("string");
        System.out.println("It is " + hasWordString + " that the string contains a word, \"string\".");

        // indexOf
        int indexOfIs = str.indexOf("m");
        System.out.println("The index of 'is' is, " + indexOfIs);

        // replace
        String replacedString = str.replace("string", "Double");
        System.out.println(replacedString);

        // split
        String[] splitString = str.split("");
        System.out.println(splitString.length);

        // substring
        String subString = str.substring(3, 10);
        System.out.println(subString);
    }
}
```

## [Array methods](#top)

<div id="array_methods" />

There is not much on arrays but there are several when we go beyond arrays to `ArrayList` and the others.

An array has the `length` attribute. It returns the size of the array.

```java
// ArrayMethods.java

public class ArrayMethods {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 4, 5, 6 };

        for (int i = 0; i < arr.length; i++) {
            System.out.println(i + "th indexed element is: " + arr[i]);
        }
    }
}
```

## [Math class](#top)

<div id="math_class" />

The Math class has some static methods we can use for some simple and complex mathematics operations. There are several but I'd mention a few. Check the reference section of the link.

-   `max(typeA x, typeA y)`: compares and returns the greater number between x and y. `typeA` can be `double|float|int|long`
-   `max(typeA x, typeA y)`: compares and returns the lesser number between x and y. `typeA` can be `double|float|int|long`
-   `ceil(double x)`: return a rounded up integer value of x.
-   `floor(double x)`: return a rounded down integer value of x.
-   `pow(int x, int y)`: returns the value of x to raised the power of y
-   `random()`: returns a random number, double, between 0 and 1
-   `sqrt(int x)`: returns the square root of x

```java
import java.util.Scanner;

// MathClass.java

public class MathClass {
    public static void main(String[] args) {
        System.out.println("The max of 3 and 5 is: " + Math.max(3, 5));
        System.out.println();

        double dValue = 1.4365;
        System.out.println("Ceil(" + dValue + "): " + Math.ceil(dValue));
        System.out.println("Floor(" + dValue + "): " + Math.floor(dValue));
        System.out.println();

        // generate 5 random numbers
        for (int i = 0; i < 5; i++) {
            System.out.println(i + 1 + "th number: " + Math.random());
        }
        System.out.println();

        // Generate random numbers between x and y, where x < y
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Min: ");
        int minValue = sc.nextInt();

        System.out.print("Enter Min: ");
        int maxValue = sc.nextInt();

        sc.close();

        for (int i = 0; i < 100; i++) {
            // cast the double in to int `(int) SOME_DOUBLE_VALUE`
            int randValue = (int) Math.floor(Math.random() * (maxValue - minValue + 1) + minValue);

            System.out.println(randValue);
        }
    }
}
```

## Conclusion

<div id="conclusion" />

A class may have methods and attributes. A class with the main can have methods but those methods must be static. It is best to make our fields/attributes private. We would use another public method to set and get the said field.

### Projects

-   Implement a class that performs arithmetic operations (limit the inputs to only integers)
-   Implement a class for a Rectangle. It must have a method to return the area and perimeter of the Rectangle. Add a static method that compares two Rectangle (if both corresponding sides are the same)

### Source

-   Sololearn
-   DS Malik
-   w3schools - [String methods][w3schools-java-string-methods], [Math class][w3schools-java-math-class]

<a href="#top">Top</a>

#

[w3schools-java-string-methods]: https://www.w3schools.com/java/java_ref_string.asp
[w3schools-java-math-class]: https://www.w3schools.com/java/java_ref_math.asp
[w3schools-java-string-methods]: https://www.w3schools.com/java/java_ref_string.asp
