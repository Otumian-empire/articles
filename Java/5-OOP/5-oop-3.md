# [A Simple Introduction To Java - Object Oriented Programming - Part 3](#top)

<div id="top"/>
In this session, we will discuss:

- [Polymorphism](#polymorphism)
- [Conclusion](#conclusion)

There four OOP concepts [Encapsulation][part-1], [Inheritance][part-2], Polymorphism and Abstraction. We have discussed the first two in the said order.

## Polymorphism

<div id="top"/>

Have you ever written a _HelloWorld_ program before? If you have then you would have noticed that the concept of _HelloWorld_ is the same across (almost) all major programming languages.

For someone who, perhaps, this is your first then let's look at the _HelloWorld_ program in _Java_, _Python_, _Javascript_ and _C++_.

### The _HelloWorld_ programs

_Java_

```java
public class HelloWorld {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}

```

This should look familiar.

_Python_

```py
print("Hello world")

```

_Javascript_

```js
console.log("Hello world");
```

_C++_

```cpp
#include <iostream>

using namespace std;

int main() {
    cout << "Hello world" << endl;

    return 0;
}

```

Even though we are doing the same thing (writing a _HelloWorld_) in all four languages, the way they do them is different. Everyone had their way of saying "Hello world". Assume that any of the implementations above is a _class_ and each _class_ has its method _sayHello: void_. Then we can say that we have _a different implementation for the same method_, _sayHello: void_. That is the bases of _Polymorphism_.

_Polymorphism_means having many forms. In the \_sayHello: void_ scenario, depending on which object that is calling the _sayHello: void_ method, we'd get a different implementation of the _sayHello: void_. There are two ways to "_polymorph_" a method in _Java_ and this is by _method overriding_ and _method overloading_.

### Overriding

Let's create a base class to work with. We would create the _Language_ class.

```java
public class Language {

    public void sayHello() {
        System.out.println("This is the Human language!!");
    }
}

```

We have a _sayHello_ method that prints, _This is the Human language!!_ to the screen. If we extend the _Language_ class, we will have access to the _sayHello_ method. The purpose of _overriding_ is to create a _polymorph_ of the method of interest.

Let's the class, `Java`

```java
public class Java extends Language {

    public void sayHello() {
        System.out.println("This is the Java language!!");
    }
}

```

and the class, `Python`

```java
public class Python {

    public void sayHello() {
        System.out.println("This is the Python language!!");
    }
}

```

and so on. Crate the classes for `Javascript` and `CPlusPlus`.

The idea is that, even though in _Inheritance_, the said classes share some common properties and methods, in _Polymorphism_ some of the methods will have a different implementation based on the object that is calling the said method.

All the classes: _Language_, _Java_, _Python_, and the rest will have the same method but with different implementations specific to each class.

If you remember the _Shape_ class, we had a default implementation for the _area_ and _perimeter_. That is the _super_ class had an implementation for _area_ and _perimeter_. In the _Square_ and _Circle_ class, the implementation for _area_ and _perimeter_ may differ so we have to _override_ them.

However, in our case where we have the _super_ class to be the _Language_ class which has just a method. _sayHello_and we are only interested in \_overriding_ it, it will be best that each of the _sub_ classes will have to stand on their own without extending the _Language_ class. We could even argue that just a class is needed with different methods like:

```java
public class SayHello {

    public void inJava() {

    }

    public void inPython() {

    }

    public void inCPluPlus() {

    }

    public void inJavascript() {

    }

}

```

Know that when we are going to _override_ a method, the _method signatures_ must be the same. So if _sayHello_ in _Language_ is `public void sayHello()` then _sayHello_ in _Java_ must be the same. For the _access modifier_, if it is _private_ from the _super_ class then we can maintain it as _private_ or we can choose a higher one like _protected_ or _public_. So we can't have a _public_ for the _super_ class' and have _protected_ or _private_ for the _sub_ class'. We can not _override_ _static_ or _final_ methods.

### Overloading

In _overriding_ a method, we have different implementations for methods by different classes. In _overloading_ we do the _overriding_ in the same class. So we'd have multiple implementations of one method.

Let's create our base class, `Sum`. `Sum` will have different implementations of a method, `add`.

> In _overriding_ a method, the _method signatures_ must be the same

By this we meant, the _access modifier_, the _return type_, the _method name_ and the _parameters_.

In _overloading_, we have the same _method name_ and _access modifier_ but the _return type_ and _parameters_ may differ.

```java
public class Sum {

    public int add() {
        return 10 + 2;
    }

    public int add(int a) {
        return a + 1;
    }

    public int add(int a, int b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }


    public double add(double a, double b) {
        return a + b;
    }

    public double add(double a, double b, double c) {
        return a + b + c;
    }


    public String add(String a, String b) {
        return a + " " + b;
    }

    public void add(String a) {
        System.out.println("We are just adding: " + a);
    }

}
```

Keep an eye on the return types and the parameters. Know that the `+`, plus, operator is also overloaded.

The question that asked is, **which method would be called**? Again, look at the _return type_ s and _parameters_. The number and type of _parameters_ you pass will determine which method to call and hence the _return type_.

## Conclusion

Polymorphism is having several forms a method. We can override the method implementation using a subclass and we can have the same method in the same class but we have different return types based on the parameters.

### Project

> This project is for the sake of practice.

Given the superclass, `Rectangle` with methods, `area` and `parameter` a subclass, `Square` that overrides the methods, `area` and `parameter`. Implement both classes.

Know that a `Rectangle` has:

- a `length` and `breadth` property.
- The `area` is the product of the properties.
- The `perimeter` is the sum of the four sides.
- Let the types be _int_.

Know that a `Square` has a

- one property that represents its sides. Since the sides are all the same. Let `length` the side be.
- The `area` is the square of its side (side by side).
- The `perimeter` is the sum of the four sides.
- Let the types be _int_.

### Source

- Sololearn
- DS Malik

<a href="#top">Top</a>

#

[part-1]: https://dev.to/otumianempire/a-simple-introduction-to-java-object-oriented-programming-part-1-60k
[part-2]: https://dev.to/otumianempire/basic-object-oriented-programming-part-2-14la
