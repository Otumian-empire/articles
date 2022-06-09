# [A Simple Introduction To Java - Object Oriented Programming - Part 4](#top)

<div id="top"/>
In this session, we will discuss:

- [Abstraction](#abstraction)
- [Interface](#interface)
- [Conclusion](#conclusion)

## Abstraction

<div id="abstraction"/>

There four OOP concepts: [Encapsulation][part-1], [Inheritance][part-2], [Polymorphism][part-3] and Abstraction. We have discussed the [Encapsulation][part-1], [Inheritance][part-2] and [Polymorphism][part-3]. Now we will consider the last of it, Abstraction.

**So what is Abstraction?**

We have been using the _Shape_ class for a while and we thank the "coiner" of the _Shape_ class.

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

Let's consider some _Plane figures_ like the _Circle_, _Square_, _Rectangle_, _Triangle_, _Parallelogram_ and the others. They have some similarities and earlier on in _Inheritance_, I mentioned that we give the similarities to the _superclass_ and the _subclasses_ inherit the _superclass_ and implement their differences. Yeah, it made sense at the time, however, this was based on the idea that they'd all the similar implementations for some methods or something like that. That idea is not bad in itself but it is flawed. Every _Shape_ should have a method of computing the _area_ and _perimeter_, but these implementations are unique to each _Shape_.

So what has _Abstraction_ got to do with this?

This is of the idea that for there to be a _Shape_ of any sort, this _Shape_ must have a method for computing the _area_ and the _perimeter_. For this idea, we will create a class that strictly enforces this concept.

An _abstract_ is kind of an _idea_, and for there to exist this _idea_, whatever model that assumes this _idea_ must conform to the _idea_. However, each model has its way of expressing this _idea_. (This sounds like _Polymorphism_)

I remember reading the [Art and Science of C][c-book] and when we got to `Chapter 8. Designing Interfaces: A Random Number Library`, the book discussed header files in the light of an API or interfaces. For this, let me share some `C` code snippets.

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

If a user, just like above, wants to use the _gcd_ and _lcm_ functions, they don't have to necessarily know about how the _gcd_ and _lcm_ functions are implemented. For someone who wants to use any of the functions, just the header file or the function definitions in the header file is enough to give the user enough information about how to use the function. The user of the functions must trust me, the designer of the function that if they call the _gcd_ function and pass in two integer arguments the _gcd_ function will return an integer.

In _Java_, we can achieve _Abstraction_ using abstract classes and interface.

Now answering the question earlier, What is Abstraction?

When we expose or provide the user of our class with the necessary information on how to use our class without giving out any information on how the class was implemented is known as Abstraction. We concentrate on the idea rather than the implementation.

### Some features of an Abstraction class

- An _Abstraction_ class is defined using the _abstract_ keyword
- We can not create an object or instance of an _Abstract_ class
- To create an instance of the _Abstract_ class, we have to create a _subclass_ of the _Abstract_ class and then create an instance of the _subclass_
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

In the above class, _name_ and _side_ are _private_. We have a single _constructor_ that takes the _name_ and _side_ as an argument. There is a getter method for _side_ since the computation of the _area_ and _perimeter_ will be based on the _side_. There are two _abstract_ methods _area_ and _perimeter_. Whatever class that extends the _Shape_ class must (has to) implement these methods. We have a default implementation for the _print_ method. This means we can override the _print_ method.

> Know that as far as a single method in a class is abstract, the whole class must become an abstract class.

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

In the Square class, we passed the name of the current _Shape_ and the dimension of the _side_ as an argument to the _Square_ _constructor_ which is then passed to the _constructor_ of the _superclass_. We implemented the _area_ and _perimeter_ methods. We will call the _print_ method when we create an instance of the _Square_ class.

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

## Interface

<div id="interface"/>

An _Interface_ is an _Abstract_ class that only has _abstract_ methods to be implemented. To create an _Interface_, we use the _interface_ keyword. Unlike the _Abstract_ classes, properties in an _interface_ can or must only be _public_, _static_ or _final_. So after they are defined, they can't be altered. An _interface_ is not "a class" so we can not <u>instantiate</u> it nor give it a _constructor_. We can _extend_ an _interface_ using another _interface_. We can "implement" several _interfaces_. In _java_ we can not extend several classes to make them an interface when then we implement them.

Since an _Interface_ is an _Abstract_ class, we don't have to add the _abstract_ or _class_ keyword when we want to create an _interface_. Just like an _Abstract_ class, all the methods in an _interface_ are _abstract_ so we don't have to declare them as _abstract_. The _abstract_ methods of an _Abstract_ class are meant to be implemented by the class that extends hence they are exposed to the public and by default all methods in an _interface_ are public.

> Remember, A subclass can have only one superclass but several interfaces to implement

Let's make an interface for our _Shape_ _abstract_ class.

```java
// IShape.java
public interface IShape {

    public double area();

    public double perimeter();

    public void print();
}

```

The preceding `I` indicates an _Interface_. To implement the _abstract_ methods, we have to create a class that will `implement` the _IShape_ interface. In place of _extends_ for a class, we use _implements_ for _Interface_.

```java
// Square.java
public class Square implements IShape {
    private double side;

    public Square(double side) {
        this.side = side;
    }

    public double area() {
        return Math.pow(this.side, 2);
    }

    public double perimeter() {
        return 4 * this.side;
    }

    public void print() {
        System.out.print("This square has an area of " + this.area());
        System.out.println(" and a perimeter of " + this.perimeter());
    }
}


```

Say we have a _Shape_ that must implement just one of the _abstract_ methods, what do we do? Remember that we have to implement all the _abstract_ methods. In a case like this, it will be enough if we split the _IShape_ to _IArea_ and _IPerimeter_, and if we want both together we can either implement both or create another _interface_, _IAreaPerimeter_.

```java
// IArea.java
public interface IArea {
    public double area();
}

```

```java
// IPerimeter.java
public interface IPerimeter {
    public double perimeter();
}

```

Consider _GumShape_ that implements _IArea_ and _overloads_ its abstract method.

```java
public class GumShape implements IArea {
    public double area() {
        return Math.PI * 3;
    }

    public double area(int s) {
        return Math.PI + s;
    }
}

```

I will update my _Main_ class:

```java
public class Main {
    public static void main(String[] args) {
        // Square square = new Square(2.5);
        // square.print();

        // Circle circle = new Circle("Circle", 7.2);
        // circle.print();

        GumShape gs = new GumShape();
        System.out.println("Gum has an area of " + gs.area(5));
    }
}

```

I didn't call the `area()` method but the `area(int s)`. If the `area` method with no parameter was not implemented, there'd be an error.

```java
public class GumShape implements IArea, IPerimeter {
    public double area() {
        return Math.PI * 3;
    }

    public double area(int s) {
        return Math.PI + s;
    }

    public double perimeter() {
        return Math.PI + 4;
    }

```

Say we have a _Shape_ that must implement just one of the _abstract_ methods, what do we do? Remember that we have to implement all the _abstract_ methods. In a case like this, it will be enough if we split the _IShape_ to _IArea_ and _IPerimeter_, and if we want both together we can either implement both or create another _interface_, _IAreaPerimeter_.

```java
// IArea.java
public interface IArea {
    public double area();
}

```

```java
// IPerimeter.java
public interface IPerimeter {
    public double perimeter();
}

```

Consider _GumShape_ that implements _IArea_ and _overloads_ its abstract method.

```java
public class GumShape implements IArea {
    public double area() {
        return Math.PI * 3;
    }

    public double area(int s) {
        return Math.PI + s;
    }
}

```

I will update my _Main_ class:

```java
public class Main {
    public static void main(String[] args) {
        // Square square = new Square(2.5);
        // square.print();

        // Circle circle = new Circle("Circle", 7.2);
        // circle.print();

        GumShape gs = new GumShape();
        System.out.println("Gum has an area of " + gs.area(5));
    }
}

```

I didn't call the `area()` method but the `area(int s)`. If the `area` method with no parameter was not implemented, there'd be an error.

```java
public class GumShape implements IArea, IPerimeter {
    public double area() {
        return Math.PI * 3;
    }

    public double area(int s) {
        return Math.PI + s;
    }

    // public double perimeter() {
    // return Math.PI + 4;
    // }
}

```

I commented out the implementation of the perimeter method as such we'd get an error. Again,

```java
public class GumShape implements IAreaPerimeter {
    public double area() {
        return Math.PI * 3;
    }

    // public double area(int s) {
    // return Math.PI + s;
    // }

    public double perimeter() {
        return Math.PI + 4;
    }
}

```

This is the same as `public class GumShape implements IArea, IPerimeter {`.

I commented out the implementation of the perimeter method as such we'd get an error. Again,

```java
public class GumShape implements IAreaPerimeter {
    public double area() {
        return Math.PI * 3;
    }

    // public double area(int s) {
    // return Math.PI + s;
    // }

    public double perimeter() {
        return Math.PI + 4;
    }
}

```

This is the same as `public class GumShape implements IArea, IPerimeter {`.

## Conclusion

<div id="conclusion"/>

Abstraction, also known as Data Abstraction, is an OOP concept where we expose the necessary information about how to use a class (and its methods) but not how the class (and its methods) are implemented. Abstraction is **implementation hiding** as _Inheritance_ is to **data hiding**.

- _Abstract_ classes are declared _abstract_ and have at least one _abstract_ method
- _Abstract_ classes can not be instantiated
- _Abstract_ classes can be _subclassed_
- _Abstract_ classes may have properties and methods
- _Abstract_ methods must be implemented by the subclass

Another to implement an Abstraction is to use an interface.

- _Interfaces_ are _Abstract_ classes
- _Interfaces_ have only _abstract_ methods
- _Interfaces_ are declared using the _interface_ keyword
- _Interfaces_ must have _public_, _static_ or _final_ properties
- _Interfaces_ can be implemented by a class using the _implements_ keyword

If you now stepping into the OOP world, [Maxi Contieri][mcsee] has a lot of articles that talk about OOP and other concepts in general. I do read his articles and I believe they will be very helpful to you as well. Consider following [Maxi Contieri][mcsee].

### Project

- Using the _Shape_ _abstract_ class implement the classes, _Rectangle_ and _Triangle_, which <u>extends</u> the _Shape_ and implements its _abstract_ methods.
- Using the _IShape_ _interface_ implement the classes, _Circle_, _Rectangle_ and _Triangle_, which <u>implements</u> the _IShape_ and implements its _abstract_ methods.

### Source

- Sololearn
- DS Malik

<a href="#top">Top</a>

#

[part-1]: https://dev.to/otumianempire/a-simple-introduction-to-java-object-oriented-programming-part-1-60k
[part-2]: https://dev.to/otumianempire/basic-object-oriented-programming-part-2-14la
[part-3]: https://dev.to/otumianempire/a-simple-introduction-to-java-object-oriented-programming-part-3-fcg
[mcsee]: https://dev.to/mcsee
[c-book]: https://cs.stanford.edu/people/eroberts/books/TheArtAndScienceOfC/index.html
