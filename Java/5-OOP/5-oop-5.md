# [A Simple Introduction To Java - Object Oriented Programming - Part 5](#top)

<div id="top"/>
In this session, we will discuss:

- [A Simple Introduction To Java - Object Oriented Programming - Part 5](#a-simple-introduction-to-java---object-oriented-programming---part-5)
  - [Anonymous Class](#anonymous-class)
  - [Inner Class](#inner-class)
  - [Enum](#enum)
  - [Conclusion](#conclusion)
  - [Problem](#problem)
    - [Source](#source)

## Anonymous Class

<div id="anonymous-class"/>

_Inheritance_ is a concept of _subclass_-ing another class, thereby having access to the opened attribute (or via setters and getters if closed) and methods. _Polymorphism_ is the concept of having many forms. It is either we can _overload_ or _override_ the said method. So we have to inherit a class we can _overload_ or _override_. With an _Anonymous_ class, we can extend the class on the fly. However, this extension only exits for the said object. So another object of the same class will not have that extension.

Say we have an _Employee_ class. Every employee gets a monthly and due to some circumstances, an employee's salary will be increased by some fraction. In such a case an employee is said to be rated.

```java
// Employee.java
public class Employee {

    private String name;
    private double salary = 200;

    public Employee(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public void calculateRate() {
        this.salary += this.salary * 0.5;
    }

    public void print() {
        System.out.println("Name: " + name);
        System.out.println("Salary: " + salary);
        System.out.println();
    }
}

```

We will create two instances of the _Employee_ class and later make one of the objects rated.

```java
// Main.java
public class Main {

    public static void main(String[] args) {
        // this is peter parker and he is not a rated employee
        Employee peter = new Employee("Peter Parker");
        peter.print();

        // this is harry potter and he is also not a rated employee
        Employee harry = new Employee("Harry Potter");
        harry.print();

        // the employer smiles on harry potter and harry becomes rated
        // management now processes harry's salary
        harry.calculateRate();
        System.out.println();

        // this is rated harry potter
        harry.print();
    }
}

```

> Consider reading through the comment on each line

Now I want to draw our attention to where harry's rate was calculated. Assuming we want to either reduce or increase the rate at which the salary is increased, what would we do? Think about this for a while.

I believe we would all agree that:

- we could pass the **rate** to the `calculateRate` method as a parameter
- we could _overload_ the `calculateRate` in the _Employee_ class
- we could _subclass_ the _Employee_ class then we'd _override_ and or _overload_ `calculateRate` method is the said _subclass_

Assuming we run into an issue like this but we don't have or want to do any of the above, we could extend the `calculateRate` method on the run. For this, let's create another _Employee_ object and set the rate to `0.15`. This is sone at where the class is instantiated.

```java
// Main.java
public class Main {

    public static void main(String[] args) {
        // this is peter parker and he is not a rated employee
        Employee peter = new Employee("Peter Parker");
        peter.print();

        // this is harry potter and he is also not a rated employee
        Employee harry = new Employee("Harry Potter");
        harry.print();

        // the employer smiles on harry potter and harry becomes rated
        // management now processes harry's salary
        harry.calculateRate();
        System.out.println();

        // this is rated harry potter
        harry.print();

        // this is john doe and is not a rated employee
        Employee john = new Employee("John Doe") {
            @Override
            public void calculateRate() {
                double johnSalary = this.getSalary();

                johnSalary += johnSalary * 0.15;
                this.setSalary(johnSalary);
            }
        };

        // the employer smiles on john so john becomes rated
        // management now processes john's salary
        john.calculateRate();
        System.out.println();

        // this is rated john doe
        john.print();

    }
}

```

When we created the `john` _Employee_, we opened the _constructor_ body, which we normally don't. We then used the `@Override` annotation and reimplemented (overrode) the `calculateRate` method.

```java

Employee john = new Employee("John Doe") {
    @Override
    public void calculateRate() {
        double johnSalary = this.getSalary();

        johnSalary += johnSalary * 0.15;
        this.setSalary(johnSalary);
    }
};

```

The `this` keyword is used to access the _getters_ and _setters_ of the _Employee_ class. The `this` keyword is in the scope of the _constructor_ body.

Overriding the _Employee_ class on the fly makes it an _Anonymous_ class for just that moment and this _overridden_ method works for just the object that implemented it.

## Inner Class

<div id="inner-class"/>

When we talk about the members of a class, then we are referring to the properties and methods. In java, we can have a class as a member of a class. This is known as a nested class. The snippet below is how I used Inner classes. It is a _User_ class which has _Inner_ classes. One for property validation, _Validation_ and the other, _Response_. _Response_ returns the response after a sign-up.

```java
// User.java
public class User {
    private static int id = 0;
    private String fullName;
    private String email;
    private String password;

    public User(String fullName, String email, String password) {
        this.fullName = fullName;
        this.email = email;
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public String getFullName() {
        return fullName;
    }

    public static int getId() {
        return id;
    }

    public User.Response signup() {
        User.Validation validation = new User.Validation();

        boolean isValidEmail = validation.email(this.email);
        boolean isValidFullName = validation.name(this.fullName);
        boolean isValidPassword = validation.password(this.password);

        User.Response response = new User.Response();

        if (isValidEmail && isValidFullName && isValidPassword) {
            User.id += 1;
            response = new User.Response(true, "Signup successful", this);
        }

        return response.getResponse();

    }

    // this is a nested class used for validating the user properties
    private class Validation {

        private boolean name(String name) {
            return !name.isEmpty() && name.trim().length() > 3;
        }

        private boolean email(String email) {
            return !email.isEmpty() && email.trim().contains("@");
        }

        private boolean password(String password) {
            return !password.isEmpty() && password.trim().length() > 2;
        }
    }

    // this is a nested class used for returning response after signup
    class Response {
        private boolean success = false;
        private String message = "Signup unsuccessful";
        private User user = null;

        // for the default values above so that when the process fails
        // I won't have to pass the success status and message
        private Response() {
        }

        private Response(boolean success, String message, User user) {
            this.success = success;
            this.message = message;
            this.user = user;
        }

        public boolean getSuccess() {
            return success;
        }

        public String getMessage() {
            return message;
        }

        public User getUser() {
            return user;
        }

        public Response getResponse() {
            return this;
        }
    }
}

```

We will create a _User_ object and call the `signup` method which then would return a _Response_ object. We take the _Response_ object and pass it to a method to print it out.

```java
// App.java
public class App {

    private static void printResponse(User.Response response) {
        System.out.println("Registration status: " + response.getSuccess());
        System.out.println("Message: " + response.getMessage());

        if (response.getSuccess()) {
            System.out.println("User");
            System.out.println("Id: " + User.getId());
            System.out.println("Full name: " + response.getUser().getFullName());
            System.out.println("Email: " + response.getUser().getEmail());
        }
    }

    public static void main(String[] args) {

        User john = new User("John Doe", "johndoe@email.com", "password");

        User.Response response = john.signup();

        printResponse(response);

    }

}

```

## Enum

<div id="enum"/>

An _Enum_ is a type used for the enumeration of constants. It is used to define a collection of constants.

If you want the days of the week, we could do:

```java
/// Day.java
public class Day {
    private int monday = 0;
    private int tuesday = 1;
    private int wednesday = 2;
    private int thursday = 3;
    private int friday = 4;
    private int saturday = 5;
    private int sunday = 6;

    public int getMonday() {
        return monday;
    }

    public int getTuesday() {
        return tuesday;
    }

    public int getWednesday() {
        return wednesday;
    }

    public int getThursday() {
        return thursday;
    }

    public int getFriday() {
        return friday;
    }

    public int getSaturday() {
        return saturday;
    }

    public int getSunday() {
        return sunday;
    }
}

```

where we would create an object of the _Day_ class and call a _getter_ to return the day we want.

Ok. What do you think is wrong with this snippet? What are we not doing well? I think we are going to be having a lot of code (_getters_) even though it is doing what we want it. What if we have about twenty (20) properties? What if we made the properties `public` and got rid of the _getters_, what do you think? Let's do it.

```java
// Day.java
public class Day {

    public int monday = 0;
    public int tuesday = 1;
    public int wednesday = 2;
    public int thursday = 3;
    public int friday = 4;
    public int saturday = 5;
    public int sunday = 6;
}

```

Waw! Now all that we want can access directly. Problem solved? Not quite. What would happen when _monday_ is altered? what will happen when any of the properties are altered? Well, we could go back and use the `private` and _getter_ approach. That will work however, we could make all the properties `final`. This way even though the properties are opened, they can't be modified. Also, we can make them `static` so that we won't have to create an object before accessing any of the days. Let's try that.

```java
// Day.java
public class Day {

    public static final int monday = 0;
    public static final int tuesday = 1;
    public static final int wednesday = 2;
    public static final int thursday = 3;
    public static final int friday = 4;
    public static final int saturday = 5;
    public static final int sunday = 6;

}

```

This way we would just do, `Day.monday` to get the numerical value (ordinal) of _monday_. The snippet about is similar to an `enum`.

```java
// Day.java
public enum Day {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
}

```

All caps are for `enum` constants is a java convention. We can have an `enum` in a file on its own and we can have it as part of a class.

```java
// DayEnum.java

public class DayEnum {

    public enum Day {
        MONDAY,
        TUESDAY,
        WEDNESDAY,
        THURSDAY,
        FRIDAY,
        SATURDAY,
        SUNDAY
    }
}

```

We can not have an `enum` inside a _constructor_ or the body of a method. (It is a sealed class). So it can exist as a member. We can not have duplicates in an `enum` as well. This is just like having duplicate attributes. We don't have to declare every property (constant) of the `enum` is `public`, `static` and `final`. So we can not alter the value of an `enum` at run time.

An `enum` can be used as a type (it is a type) just as an `int` or `String` could be used. We can pass it as a type to a parameter.

```java
public static void printDay(Day day) {
    System.out.println("Today is, " + day.name().toLowerCase());
}

```

`enum` has a `name()` method which returns the name of the `enum` value. This will be in uppercase since we used uppercase to define the `enum` constants. The `toString()` method does the same.

```java
public static void printDayToString(Day day) {
    System.out.println("Today is, " + day.toString());
}

```

We can the integer constant (ordinal) of an `enum` constant using the `ordinal()` method.

```java
public static void printOrdinal(Day day) {
    System.out.println("The ordinal for " + day.name() + " is " + day.ordinal());
}
```

We can get an `enum` constant when we pass its `String` name to the `valueOf` method, `valueOf(String name)`. We'd get an error if the name passed doesn't exist.

```java
System.out.println(Day.valueOf("MONDAY"));
```

We can compare one `enum` constant to another using the `compareTo` method, `compareTo(Enum o)`. This returns the difference between the two constants.

We can also check for equality between enum constants using the `equal` method, `equal(Enum o)`. It returns a `boolean`.

```java
System.out.println(day.equals(Day.FRIDAY));
```

We can loop through the `enum` constants. The static method `values()` returns an array of the `enum` constants.

```java
    for (Day d : Day.values()) {
        System.out.println(d);
    }
```

An `enum` can have methods.

**All the Snippet for the `enum`:**

```java
// DayEnum.java

public class DayEnum {
    public enum Day {
        MONDAY,
        TUESDAY,
        WEDNESDAY,
        THURSDAY,
        FRIDAY,
        SATURDAY,
        SUNDAY;

        public void salutation() {
            System.out.println("Hey, today is " + this.name().toLowerCase());
        }
    }

    public static void printDay(Day day) {
        System.out.println("Today is, " + day.name().toLowerCase());
    }

    public static void printDayToString(Day day) {
        System.out.println("Today is, " + day.toString());
    }

    public static void printOrdinal(Day day) {
        System.out.println("The ordinal for " + day.name() + " is " + day.ordinal());
    }

    public static void main(String[] args) {
        Day day = Day.THURSDAY;

        printDay(day);

        printDayToString(day);

        printOrdinal(day);

        System.out.println(Day.valueOf("MONDAY"));

        System.out.println(day.compareTo(Day.MONDAY));

        System.out.println(day.equals(Day.FRIDAY));

        for (Day d : Day.values()) {
            System.out.println(d);
        }

        day.salutation();
    }
}
```

## Conclusion

<div id="conclusion"/>

_Anonymous_ classes provide a means to _override_ a method on the fly. This is done by opening the _constructor_ using the `@Override` annotation to _overrode_ the said method. The method _overridden_ is only available to the object the _overrode_ it.

An _Inner_ class is a class nested in a class as a member of the class.

## Problem

- Read more on `enum`

### Source

- Sololearn
- DS Malik

<a href="#top">Top</a>
