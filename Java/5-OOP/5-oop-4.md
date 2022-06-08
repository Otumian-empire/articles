# [A Simple Introduction To Java - Object Oriented Programming - Part 4](#top)

<div id="top"/>
In this session, we will discuss:

- [Abstraction](#abstraction)
- [Interface](#interface)
- [Inner Class](#inner_class)
- [Conclusion](#conclusion)

## Abstraction

<div id="abstraction"/>

There four OOP concepts: [Encapsulation][part-1], [Inheritance][part-2], [Polymorphism][part-3] and Abstraction. We have discussed the [Encapsulation][part-1], [Inheritance][part-2] and [Polymorphism][part-3]. Now we will consider the last of it, Abstraction.

So what is Abstraction?

We having been using using the _Shape_ class for a while and we thank the "coiner" of _Shape_ class.

This is one of the early implementations of the _Shape_ class:

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

According to this class, we assume that every _Shape_ has _length_ and _breadth_ as properties, and every _Shape_ has a method for computing the _area_ and _perimeter_ of the said _Shape_. However pleasant and useful it was, there were some flaws in the implementation and the idea as a whole.

> The _Shape_ class was based on _Plane figures_.

Let's consider some _Plane figures_ like the _Circle_, _Square_, _Rectangle_, _Triangle_, _Parallelogram_ and the others. They are have some similarities and earlier on in _Inheritance_, I made mention that we give the similarities to the _superclass_ and the _subclasses_ inherit the _superclass_ and implement their differences. Yeah, it made sense at the time, however this was based on the idea that they'd all the similar implementations for some methods or something like that. That idea is not bad in itself but it flawed. Every _Shape_ should have a method of computing the _area_ and _perimeter_, but these implementations are unique to each _Shape_.

So what has _Abstraction_ got to do with this?

This is of the idea that for there to be a _Shape_ of any sort, this _Shape_ must have a method for computing the _area_ and the _perimeter_. For this idea, we will create a class that strictly enforces this concept.

An _abstract_ is kind of an _idea_, and for there to exist this _idea_, whatever model that assumes this _idea_ must conform to the _idea_. However, each model has its own way of expressing this _idea_. (This sounds like _Polymorphism_)

<!-- TODO: Get the url to the book  -->

I remember reading the _Art and Science of C_ and when we got to header files, the book discussed header files in the light of an API or interfaces. For this, let me share some `C` code snippet.

```C
/*
gcdlcm.c

A program that computes the gcd and lcm of two integers, x and y
*/

#include <stdio.h>

/* function definition of gcd */
int gcd(int x, int y);

/* function definition of lcm */
int lcm(int x, int y);

// entry point
int main()
{
    int x = 12, y = 18;

    printf("The gcd of %d and %d is %d\n", x, y, gcd(x, y));

    printf("The lcm of %d and %d is %d\n", x, y, lcm(x, y));
}

/* function implementation for gcd */
int gcd(int x, int y)
{
    if (y == 0)
    {
        return x;
    }

    return gcd(y, x % y);
}

/* function implementation for lcm */
int lcm(int x, int y)
{
    return (x * y) / gcd(x, y);
}

```

We can compile this snippet by running, `gcc gcdlcm.c` then `./a.out` (Linux here). The output was,

```sh
The gcd of 12 and 18 is 6
The lcm of 12 and 18 is 36

```

> In my own words

If a user, just like above, wants to use the _gcd_ and _lcm_ functions, they don't have to necessarily know about how the _gcd_ and _lcm_ functions are implemented. For someone who wants to use any of the functions, just the header file or the function definitions in the header file is enough to give the user enough information about how to use the function. The user of the functions must trust the me, the designer of the function that if they call the _gcd_ function and pass in two integer argument the _gcd_ function will return an integer.

In _Java_, we can achieve _Abstraction_ using abstract classes and interface.

Now answering the question earlier, What is Abstraction?

When we expose or provide the user of our class with the necessary information on how to use our class without giving out any information on how the class was implemented is known as Abstraction. We concentrate on the idea rather than the implementation.

### Some features of an Abstraction class

- An _Abstraction_ class is defined using the _abstract_ keyword
- We can not create an object or instance of an _Abstract_ class
- To create an instance of the _Abstract_ class, we have to create a _subclass_ of the _Abstract_ class and then create instance of the the _subclass_
- An _Abstract_ class may have _Abstract_ methods (An _Abstract_ method is that with a method definition without implementation - just like in the _gcd_ and _lcm_)
- An _Abstract_ class may have properties and methods just like any other class
- The _Abstract_ methods must be implemented by the subclass

### Some examples

Let's provide a different implementation of the _Shape_ class. We will make the _Shape_ class an _abstract_ class and make the _area_ and _perimeter_ methods _abstract_ as well.

```java
public abstract class Shape {
    private String name;
    private double side;

    public Shape(String name, double side) {
        this.name = name;
        this.side = side;
    }

    public double getSide() {
        return this.side;
    }

    // abstract methods
    public abstract double area();

    public abstract double perimeter();

    // default methods
    public void print() {
        System.out.print("This " + this.name + " has an Area of "
                + this.area() + " squared units");

        System.out.println(" and a Perimeter of "
                + this.perimeter() + " units.");
    }
}

```

In the above class, _name_ and _side_ are _private_. We have a single _constructor_ that takes the _name_ and _side_ as argument. There is a getter method for _side_ since in the computation of the _area_ and _perimeter_ will be based on the _side_. There are two _abstract_ methods _area_ and _perimeter_. Whatever class that extends the _Shape_ class must (has to) implement these methods. We have a default implementation for the _print_ method. This mean we can override the _print_ method.

> Know that as far as a single method in a class is abstract, the whole class must become abstract class.

Since we can not create an instance of the _Shape_ class, let's create another _Shape_, _Square_ that will inherit the _Shape_ class. (This is like _Inheritance_ and _Polymorphism_ bundled together)

```java
public class Square extends Shape {

    public Square(String name, double side) {
        super(name, side);
    }

    /* area = side * side or side squared */
    public double area() {
        return Math.pow(this.getSide(), 2);
    }

    /* perimeter = side + side + side + side or 4 * side */
    public double perimeter() {
        return 4 * this.getSide();
    }
}

```

In the Square class, we passed the name of the current _Shape_ and the dimension of the _side_ as argument to the _Square_ _constructor_ which are then passed to the _constructor_ of the _superclass_. We implemented the _area_ and _perimeter_ methods. We will call the _print_ method when we create an instance of the _Square_ class.

```java
public class Main {
    public static void main(String[] args) {
        Square square = new Square("Square", 2.5);
        square.print();
    }
}
// Output:
// This Square has an Area of 6.25 squared units and a Perimeter of 10.0 units.
```

Let's add another _Shape_ class, _Circle_.

```java
public class Circle extends Shape {
    public Circle(String name, double radius) {
        super(name, radius);
    }

    /* area = PI * radius * radius or PI * radius squared */
    public double area() {
        return Math.round(Math.PI * Math.pow(this.getSide(), 2));
    }

    /*
     * A Circle's perimeter is the same as its circumference
     * perimeter = 2 * PI * radius
     */
    public double perimeter() {
        return Math.round(2 * Math.PI * this.getSide());
    }
}

```

From the implementation of the _area_ and _perimeter_ methods, it is obvious that these are different from that of the _Square_ class. I added the `round` method from the `Math` class. Now we can create an instance of the _Circle_ class and call its _print_ method.

```java
public class Main {
    public static void main(String[] args) {
        Square square = new Square("Square", 2.5);
        square.print();

        Circle circle = new Circle("Circle", 2.5);
        circle.print();
    }
}
// output:
// This Square has an Area of 6.25 squared units and a Perimeter of 10.0 units.
// This Circle has an Area of 163.0 squared units and a Perimeter of 45.0 units.
```

## Conclusion

<div id="conclusion"/>

### Project

- Using the _Shape_ _abstract_ class implement, _Rectangle_ and _Triangle_ which inherit the _Shape_ class and implements its _abstract_ methods.

### Source

- Sololearn
- DS Malik

<a href="#top">Top</a>

#

[part-1]: https://dev.to/otumianempire/a-simple-introduction-to-java-object-oriented-programming-part-1-60k
[part-2]: https://dev.to/otumianempire/basic-object-oriented-programming-part-2-14la

<!-- TODO: get the url for the polymorphism article -->
