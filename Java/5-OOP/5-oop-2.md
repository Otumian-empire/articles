# [Basic Object Oriented Programming - Part 2](#top)

<div id="top"/>
In this session, we will discuss:

- [Inheritance](#inheritance)
- [Conclusion](#conclusion)

In the previous chapter, we discussed the `Shape` class and the concept of _Encapsulation_. The `Shape` class can be summarized as:

- length: `double`
- breadth: `double`
- area(): `double`
- perimeter(): `double`
- print(): `void`

We said that:

> **Encapsulation** means <u>data hiding</u>, making use of the `private` keyword which restricts access to _fields_ or and _methods_ declared as `private`.

<div id="inheritance"/>

## Inheritance

Squares, Rectangles, Circles, and others are plane figures or shapes. We defined the `Shape` class with the above _fields_ and _methods_. Can you implement a class for Square, rectangle, Circle, etc without some or all the _fields_ and _methods_? Of course, you can.

What is the point of _Inheritance_?

When given two classes say class A and B. if class B happens to share the same _fields_ and _methods_ as class A, then in the implementation of class B we would only have to create a class for the class that will have all the _fields_ and _methods_ of class A then we'd add the _fields_ and _methods_ that are not available in class A.

So in Inheritance, one class will have the _fields_ and _methods_ of another class. That is it.

The common terms one hears of most often are inheritance, extending, sub-classing and others (create a class based on another class).

### Super and Sub Class

A _super class_, also known as a parent or a base class, is the class from which other classes are created. In science class, we had fundamental quantities like mass, length, time, etc. We then derive other quantities such as velocity and her friends.

A _sub class_, also known as a child or a derived class, is the class that is created/derived from another. From science class, we had derived quantities like area, volume, and velocity and her brothers were created from a combination of other quantities such as length, time, etc.

### Extending A Class

Given a class _A_:

```java
public class A {

}
```

Another class _B_ will inherit the properties of class _A_ as:

```java
public class B extends A {

}
```

So to extend a class we use the `extends` keyword.

### Create the Human-Student-Teacher class

Is there any difference between a student and a teacher? Are there features and abilities one has over the other? Are there any similarities between them?

Let's see some <u>similarities</u>.

- Full name or just name
- Date of birth
- Both are hairy in some way or the other
- They would have each have their IDs
- etc

Let's see some <u>distinctions</u>.

- A teacher is a _stuff_ of the school and a student is not. A teacher can teach the class but a student can't do that.
- A teacher receives a _salary_ at the end of the month but the student has to pay fees for the academic year.
- etc

The idea is that we group the attributes that both have and we create a class for that. Then each entity will inherit that parent class and add its attributes and methods.

A teacher and a student are both human so we can create a class called _Human_ that can serve as the **base** _class_.

```java
// Human.java
public class Human {

    private String id;
    private String password;
    private String fullName;

    public Human() {
    }

    public Human(String id, String password, String fullName) {
        this.id = id;
        this.password = password;
        this.fullName = fullName;
    }

    public String getId() {
        return this.id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPassword() {
        return this.password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getFullName() {
        return this.fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }
}

```

Now, the _Human_ class doesn't need much elaboration. We can create a _Student_ class without creating a _constructor_ (we'd use the default/empty _constructor_).

```java
// Student.java
public class Student extends Human {

    public Student() {
    }

}
```

In the _Main_ class, we can use the _getter_ and _setter_ methods to manipulate the properties of the _Student_ object that we will create.

```java
// Main.java
public class Main {

    public static void main(String[] args) {
        Student student = new Student();

        // set the properties of the class using
        student.setId("std0012");
        student.setFullName("John Adams");
        student.setPassword("simple_password");

        System.out.println("Full Name: " + student.getFullName());
        System.out.println("ID: " + student.getId());
        System.out.println("Password: " + student.getPassword());
    }
}
```

You know, we can also add a _constructor_ to the _Student_ class so that it will have the same _constructor_ signature as its parent class. We can achieve this by calling the _constructor_ of the parent class. **We don't have to redefine the properties that are defined in the parent class.** We just have to pass them as parameters. To achieve this, we can use the `super` function that `java` provides. We will use the `super` function as a normal _constructor_.

```java
// Main.java
public class Student extends Human {

    public Student() {
    }

    public Student(String id, String password, String fullName) {
        super(id, password, fullName);
    }

}
```

And now, our Main class will look like

```java
// Main.js
public class Main {

    public static void main(String[] args) {
        // set the properties of the class using
        /*
         * Student student = new Student();
         *
         * student.setId("std0012");
         * student.setFullName("John Adams");
         * student.setPassword("simple_password");
         */

        // Use the student constructor
        Student student = new Student("std0012", "simple_password", "John Adams");

        System.out.println("Full Name: " + student.getFullName());
        System.out.println("ID: " + student.getId());
        System.out.println("Password: " + student.getPassword());
    }
}
```

What happens in `super(id, password, fullName);`?

This is the same as calling the constructor of the _super_ class and passing in the necessary arguments.

Let's say we want to add a new property to the _Student_ class, we can do so simply as:

```java
// Student.java
public class Student extends Human {

    private boolean isClassRep;

    public Student() {
    }

    public Student(String id, String password, String fullName) {
        super(id, password, fullName);
    }

    // new constructor with a fourth parameter for isClassRep
    public Student(String id, String password, String fullName, boolean isClassRep) {
        super(id, password, fullName);
        this.isClassRep = isClassRep; // not added to super
        // this.setClassRep(isClassRep); // same as the above
    }

    public boolean isClassRep() {
        return this.isClassRep;
    }

    public void setClassRep(boolean isClassRep) {
        this.isClassRep = isClassRep;
    }

}
```

As we can see, I add a new property, `isClassRep` and created a new _constructor_ which allows us to pass the new property as part of the _Student_ _constructor_. I did that so that we can still maintain the parent signature.

```java
// Main.java
public class Main {

    public static void main(String[] args) {
        // set the properties of the class using
        /*
         * Student student = new Student();
         *
         * student.setId("std0012");
         * student.setFullName("John Adams");
         * student.setPassword("simple_password");
         */

        // Use the student constructor
        Student student = new Student("std0012", "bunny", "John Adams");

        System.out.println("Full Name: " + student.getFullName());
        System.out.println("ID: " + student.getId());
        System.out.println("Password: " + student.getPassword());
        System.out.println();

        // student object with isClassRep
        Student studentRep = new Student("std0013", "password", "Hannah Adams", true);

        System.out.println("Full Name: " + studentRep.getFullName());
        System.out.println("ID: " + studentRep.getId());
        System.out.println("Password: " + studentRep.getFullName());
        System.out.println(studentRep.getFullName() + " is class president: " + studentRep.isClassRep());
    }
}
```

You can create the _Teacher_ class that extends the _Human_ class. Add an attribute for `isClassTeacher: boolean`, and also the teacher's salary, `salary: int`.

What would we do if we want to add an attribute to the class called `hobby: String`? Try it out.

## Conclusion

<div id="conclusion" />

One class may share the _properties and methods_ of another class through `Inheritance`. In `java`, we use the `extends` keyword to indicate that a class is being inherited. The class whose methods and attributes are inherited is called the _super_ class and the class which does the inheriting is called the _sub_ class. We can make use of the _constructor_ of the _super_ class using the _super_ keyword and then passing the necessary arguments.

### Projects

Let's consider the one-dimensional shape class, _Shape_. Inherit this class and create the _Square_ and _Rectangle_ _sub_ classes with the appropriate attribute(s) and methods to:

- `describe(): void` -> to describe the shape
- `area(): int` -> to return the area of the said shape
- `perimeter(): int` -> to return the perimeter of the said shape

```java
// Shape.java
public class Shape {
    private int side;

    public Shape(int side) {
        this.side = side;
    }

    public int getSide() {
        return this.side;
    }

    public void setSide(int side) {
        this.side = side;
    }

}
```

### Source

- Sololearn
- DS Malik
- vscode (code generation)

<a href="#top">Top</a>
