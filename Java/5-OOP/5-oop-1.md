# [Basic Object Oriented Programming - Part 1](#top)

<div id="top"/>
In this session, we will discuss:

-   [Shape class](#Shape_class)
-   [Encapsulation](#encapsulation)
-   [Package](#package)
-   [Conclusion](#conclusion)

We have already looked at how to create functions or methods and also how to create classes. You should refer to [Class and Method](https://dev.to/otumianempire/a-simple-introduction-to-java-class-and-method-2mj1).

<div id="Shape_class"/>

## Shape Class

The purpose of creating the `Shape` class is to demonstrate the use of the `this` keyword in java. The `this` keyword refers to the instance of the class and we can use it with the `.` operator to access the properties/fields and methods of the class anywhere in the said class.

> Create a class, `Shape`.

Let the `Shape` class have the following attributes and methods:

-   length: `double`
-   breadth: `double`
-   area(): `double`
-   perimeter(): `double`

> The methods have the `()`

The above ADT tells us that the class has two fields and two methods, the types and return types. It doesn't tell us how the methods are implemented. Try an implement the `Shape` class.

```java
public class Shape {
    double length;
    double breadth;

    public Shape(double length, double breadth) {
        length = length;
        breadth = breadth;
    }

    public double area() {
        return length * breadth;
    }

    public double perimeter() {
        return 2 * (length + breadth);
    }
}
```

What do you notice when you execute the Shape class?

```java
// Main.java
public class Main {

    public static void main(String[] args) {
        Shape s = new Shape(2.5, 2.6);
        System.out.println("Area: " + s.area());
        System.out.println("Perimeter: " + s.perimeter());
    }
}
```

It will appear that the output will become:

```
Area: 0.0
Perimeter: 0.0
```

But why the `0.0`s? This was because of our constructor. If you remember so far all our constructors have different names compared to the fields.

Replace the constructor with the snippet below:

```java
public Shape(double l, double b) {
    length = l;
    breadth = b;
}
```

Now the output looks more correct and as expected just like the result below.

```
Area: 6.5
Perimeter: 10.2
```

Using different variable names was another way to solve the previous issue we had where all the outputs were `0.0`. We could have used the `this` keyword.

Change the constructor to the snippet below:

```java
public Shape(double length, double breadth) {
    this.length = length;
    this.breadth = breadth;
}
```

The output will be the same as the above. Using the same parameter names as the field names make our code, to some degree, self-documenting. What would `l` and `b` mean anyway?

We can use the `this` keyword on the rest of the fields called in the `area` and `parameter` methods too. We should add void methods to print the area and perimeter with some text, informing the user or displaying the length and breadth of the shape. Let's call this method `print`.

Our new `Shape` ADT will be:

-   length: `double`
-   breadth: `double`
-   area(): `double`
-   perimeter(): `double`
-   print(): `void`

Now our new class will look like the snippet below:

```java
public class Shape {
    double length;
    double breadth;

    public Shape(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    public double area() {
        return this.length * this.breadth;
    }

    public double perimeter() {
        return 2 * (this.length + this.breadth);
    }

    public void print() {
        System.out.println("The shape has a length and a breadth of, "
                + this.length + " and " + this.breadth + ".");
        System.out.println("Shape has an Area of " + this.area()
                + " squared units.");
        System.out.println("Shape has a Perimeter of " + this.perimeter()
                + " units.");
    }
}
```

Our little output will be:

```
The shape has a length and a breadth of, 2.5 and 2.6.
Shape has an Area of 6.5 squared units.
Shape has a Perimeter of 10.2 units.
```

<div id="encapsulation"/>

## Encapsulation

In java, there are four main concepts that we have to understand about Object-Oriented-Programming. These are Encapsulation, Inheritance, Polymorphism and Abstraction.

We'd discuss Encapsulation here and discuss the other three in a separate article.

So, what is Encapsulation? Do you remember what we discussed about access modifiers? We said access modifiers regulate access to class methods and variables. There are `public`, `protected`, `private` and `default`. The `private` access modifier restricts the access to methods or variables declared as `private` outside the class. The concept of Encapsulation revolves around the `private` access modifier and how to resolve the problems that arise when the `private` access modifier is used.

We can prevent the user of our class from directly accessing and modifying the state of the objects they create. This is done to hide implementation details from the user. We provide the user of our class with some `public` methods to access the variables and or methods that we have declared `private`.

If we consider the `Shape` class, the `length` and `breadth` have no access modifiers. Well, they do, it's just that we didn't specify it. So it is by "default", `default`. What this means is that the fields can be accessed by another class in the same package as the `Shape` class.

### Getters and Setters

I mentioned earlier that, we can hide implementation details by declaring some fields or methods `private` than allowing indirect access to these fields and methods via some `public` methods. These methods are known as `getters` and `setters`.

Let's experiment. Make the `fields` in the `Shape` class `private` and in the `Main` class, comment out `s.print();` and do, `System.out.println(s.length);`. What happened?

Well, on my side, I am using vscode and before I even completed the whole print statement a red squiggly line appear below the print statement. Saying, _The field Shape.length is not visible_. In vscode, neither `length` nor `breadth` showed up on the IntelliSense.
Now we know that when we make a field `private` the `field` will be inaccessible outside the class.

Now let's talk about `getters` and `setters`, what they are and how to use them.

We made the `length` and `breadth` fields `private` which means we can not access them nor write them. We can not read their value nor can we reassign or update their value. With a `public` _getter_ method, we can return the said `private` field. So if the return type of `length` is `int`, the _getter_ will return an `int` value which is the `private` field. A setter is a `public` method with no return type. Its return type is void. We use a _setter_ to set a value for a `private` field. Something like assigning a `private` field a new value via some method. So the _setter_ method will take the value as an argument and reassign the `private` field with the passed argument.

The _getter_ method looks like the snippet below:

```java
public [type] getPrivateField() {
    return this.privateField;
}
```

`[type]` is just the data type. The _getter_ method name starts with `get` (which indicates that it is a _getter_ method). The remaining part is mostly the name of the private field.

The goes for the _setter_ method but in place of "get" we use "set".

The _setter_ method looks like the snippet below:

```java
public void setPrivateField([type] someValue) {
    this.privateField = someValue;
}
```

Know that the type of `someValue` and the said `private` field must have the same type.

With this new information, update the `Shape` class using `getters` and `setter`.

This is what my `Shape` class now looks like after the new changes:

```java
public class Shape {
    private double length;
    private double breadth;

    public Shape(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }

    public double getBreadth() {
        return breadth;
    }

    public void setBreadth(double breadth) {
        this.breadth = breadth;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double area() {
        return this.length * this.breadth;
    }

    public double perimeter() {
        return 2 * (this.length + this.breadth);
    }

    public void print() {
        System.out.println("The shape has a length and a breadth of, "
                + this.length + " and " + this.breadth + ".");
        System.out.println("Shape has an Area of " + this.area()
                + " squared units.");
        System.out.println("Shape has a Perimeter of " + this.perimeter()
                + " units.");
    }
}
```

Now in the `Main` class, instead of `System.out.println(s.length);` we can now do, `System.out.println(s.getLength());`.

What do you think about `getters` and `setters`? Well, what I noticed is that, if I don't need direct access to the fields, I don't need `getters` and `setters`. In the `Main` class, if we have nothing to do with the fields then we don't need `getters` and `setters`. Apart from setting the fields using the constructors, there hasn't been anywhere the fields were set so we can do away with the `setters`. Know when to use the `getters` and `setters`. The basic knowledge here is restricting access.

Have a look at the `print` method in the `Shape` class.

```java
 public void print() {
    System.out.println("The shape has a length and a breadth of, "
            + this.length + " and " + this.breadth + ".");
    System.out.println("Shape has an Area of " + this.area()
            + " squared units.");
    System.out.println("Shape has a Perimeter of " + this.perimeter()
            + " units.");
    }
```

We can comment out the `print` method and put its body in the `Main` class where we placed `System.out.println(s.getLength());`. We would have to change `this` to `s` and then use the `getters` in place of the fields. Mine `Main` class now looks like this:

```java
public class Main {
    public static void main(String[] args) {
        Shape s = new Shape(2.5, 2.6);
        // s.print();
        System.out.println("The shape has a length and a breadth of, "
                + s.getLength() + " and " + s.getBreadth() + ".");
        System.out.println("Shape has an Area of " + s.area()
                + " squared units.");
        System.out.println("Shape has a Perimeter of " + s.perimeter()
                + " units.");
    }
}
```

And the output I got was,

```
The shape has a length and a breadth of, 2.5 and 2.6.
Shape has an Area of 6.5 squared units.
Shape has a Perimeter of 10.2 units.
```

Note that it is advised to let a class do one thing. This was why I said we should come out of the print method. Even though we create the `getters` and `setter` for external use, we can also use them internally.

In the constructor, instead of assigning a `private` field a value by assignment, use the _setter_. In the `perimeter` and `area` methods, use the _getters_.

<div id="package"/>

## Package

You may have heard of the term, Package at least once in your life as a human. I mean, as a java programmer you'd be dealing with packages a lot. So take what you know and translate that thought to java.

Do you know java has a `Math` class? What about we create our own `Math` class without the names of the classes conflicting. How do we do that? We use a `package`. A package is just a folder. For our case as starters, the package just sits right in our root directory. There are some benefits to using `packages` which include:

-   we can group related classes which will make it easier to debug and maintain the codebase.
-   this prevents the pollution of namespaces, no name will class with another.
-   by default, packages restrict the access of class to outsiders but are open to the classes in the said `package`.

### Create MyMath Package

To create a package all we have to do is create a folder and then create our classes in that folder.

> Let's create a folder, `MyMath` in the root of project files. Now inside `MyMath` folder, create a java class, `Math`

Now at the very top before the class header, put `package MyMath;`. This indicates that `Math` class is a file in the `MyMath` `package`.

My `Math` class looks like this:

```java
package MyMath;

public class Math {

}
```

Let's add two methods, `addOne(int num): int` and `incBy(int num, int val): int`. So as the method name suggests about their implementation, the `addOne` method takes an `int` argument and adds one to it then returns the result. `incBy` takes two arguments, `num` and `val`. It adds `val` to `num` and returns the result. Since all the methods in the `Math` class `static` methods, let's make ours also `static`.

```java
package MyMath;

public class Math {
    public static int addOne(int num) {
        return num + 1;
    }

    public static int incBy(int num, int val) {
        return num + val;
    }
}
```

In the `Main` class, let's clear the `main` method's body. Now to use the new package we have created, we have to import it in the `Main` class as `import MyMath.Math;`

So our `Main` class will now look like this:

```java
import MyMath.Math;

public class Main {
    public static void main(String[] args) {
        System.out.println(Math.addOne(1));
        System.out.println(Math.incBy(1, 3));
    }
}
```

There is a problem here. We can use our `Math` class freely now but what about the java `Math` class? Of course, we can use the java `Math` class anywhere but we can not do that in our `Math` class. It is for reasons like that we use packages.

I used the pascal case for my package name, the recommended approach is to have a _root_ folder, then in the _root_ folder, you'd have your _package_ folder then your _classes_. so you'd import it as `import root.package.ClassName;`. Note the use of the lower case for the root and package names. This is similar to `import java.util.Scanner;`.

<div id="conclusion"/>

## Conclusion

-   OOP is a programming paradigm where classes are used to model real-life objects.
-   There are four main concepts of OOP: _Encapsulation_, _Inheritance_, _Polymorphism_ and _Abstraction_.
-   **Encapsulation** means <u>data hiding</u>, making use of the `private` keyword which restricts access to _fields_ or and _methods_ declared as `private`.
-   We make use of _getters_ and _setters_ to make `private` _fields_ or and _methods_ available to classes outside the said class.
-   We can use packages to group related classes and this prevents namespace pollution.

### Projects

The projects here will be simple (not easier). We would implement the back account program using the knowledge we've acquired so far.

-   A bank account has an account name, account number and pin.
-   One can deposit and redraw from one's bank account.
-   One can check their balance.
-   After a withdrawal or a deposit, display a message saying how much the account owner previously had before the transaction was made, the amount used in the transaction and what their new balance is.
-   We can not have a balance less than zero and we can not deposit nor withdraw a negative amount from the balance.
-   Make the program interactive by asking the user to input their account name, number and pin when the program is first executed.
-   Assign the user an initial balance of 100.
-   Provide an interactive means for the user to deposit, withdraw or exit the program.

> TIPS: Have a different class for the bank account and another for the interactivity (the main class will also do). Use integers for the amounts. If you think you can add some functionality that is not mentioned, do so.

### Source

-   Sololearn
-   DS Malik

<a href="#top">Top</a>
