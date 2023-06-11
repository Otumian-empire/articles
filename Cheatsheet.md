# C# CheatSheet

## BASIC

- **Data types**

  - Integers: `int`, `long`, `short`, `byte`
  - Floating-point numbers: `float`, `double`, `decimal`
  - Booleans: `bool`
  - Characters: `char`
  - Strings: `string`
  - Arrays: `array`
  - Lists: `list`
  - Dictionaries: `dictionary`

- **Operators**

  - Arithmetic operators: `+`, `-`, `*`, `/`, `%`
  - Logical operators: `&&`, `||`, `!`
  - Relational operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - Bitwise operators: `&`, `|`, `^`, `~`
  - Assignment operators: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `~=`

- **Control flow statements**

  - If statement: `if (condition) { statement; }`
  - Else statement: `if (condition) { statement; } else { statement; }`
  - Switch statement: `switch (expression) { case value: statement; break; case value: statement; break; default: statement; }`
  - While loop: `while (condition) { statement; }`
  - Do-while loop: `do { statement; } while (condition);`
  - For loop: `for (int i = 0; i < 10; i++) { statement; }`
  - For each loop: `foreach (var item in list) { statement; }`

- **Functions**

  - Function declaration: `public void MyFunction() { statement; }`
  - Function call: `MyFunction();`
  - Parameters: `public void MyFunction(int parameter1, string parameter2) { statement; }`
  - Return values: `public int MyFunction() { return 10; }`

- **Classes**

  - Class declaration: `public class MyClass {}`
  - Object instantiation: `var myObject = new MyClass();`
  - Properties: `public string Name { get; set; }`
  - Methods: `public void MyMethod() { statement; }`
  - Events: `public event EventHandler MyEvent;`

- **Other**

  - Comments: `// This is a comment.`
  - Namespaces: `using System;`
  - Imports: `import static System.Console;`
  - LINQ: `var query = from item in list where item.Name == "John" select item;`
  - Exceptions: `try { statement; } catch (Exception e) { statement; }`

## OOP

- **Abstraction:** Abstraction is the process of hiding the implementation details of an object and only exposing the essential details to the user. This makes the object easier to use and understand.
- **Encapsulation:** Encapsulation is the process of grouping together related data and methods into a single unit. This makes the code more organized and easier to maintain.
- **Inheritance:** Inheritance is the ability of one class to inherit the properties and methods of another class. This makes it possible to reuse code and create more complex objects.
- **Polymorphism:** Polymorphism is the ability of an object to behave differently depending on its type. This makes it possible to create more flexible and reusable code.

Here are some examples of OOP in C#:

- A `Car` class might have properties for the car's make, model, and year, as well as methods for starting the car, driving the car, and turning off the car.
- A `BankAccount` class might have properties for the account's balance, owner, and type, as well as methods for depositing money, withdrawing money, and transferring money.
- A `Person` class might have properties for the person's name, age, and address, as well as methods for getting the person's age, changing the person's address, and printing the person's information.

## OOP Code

```c#
// Abstraction
public abstract class Car
{
    public abstract void Start();
    public abstract void Drive();
    public abstract void TurnOff();
}

// Encapsulation
public class BankAccount
{
    private int balance;
    private string owner;
    private AccountType type;

    public int Balance
    {
        get { return balance; }
        set { balance = value; }
    }

    public string Owner
    {
        get { return owner; }
        set { owner = value; }
    }

    public AccountType Type
    {
        get { return type; }
        set { type = value; }
    }

    public void Deposit(int amount)
    {
        balance += amount;
    }

    public void Withdraw(int amount)
    {
        if (balance < amount)
        {
            throw new InsufficientFundsException();
        }

        balance -= amount;
    }

    public void Transfer(int amount, BankAccount otherAccount)
    {
        this.Withdraw(amount);
        otherAccount.Deposit(amount);
    }
}

// Inheritance
public class CheckingAccount : BankAccount
{
    public CheckingAccount(string owner, int balance)
        : base(owner, balance, AccountType.Checking)
    {
    }
}

public class SavingsAccount : BankAccount
{
    public SavingsAccount(string owner, int balance)
        : base(owner, balance, AccountType.Savings)
    {
    }

    public void AddInterest()
    {
        balance += balance * 0.01;
    }
}

// Polymorphism
public interface IAnimal
{
    void Speak();
}

public class Dog : IAnimal
{
    public void Speak()
    {
        Console.WriteLine("Woof!");
    }
}

public class Cat : IAnimal
{
    public void Speak()
    {
        Console.WriteLine("Meow!");
    }
}
```

## Methods

```c#
// Arrays
int[] myArray = new int[] { 1, 2, 3, 4, 5 };

// Lists
List<string> myList = new List<string> { "Hello", "World" };

// Dictionaries
Dictionary<string, string> myDictionary = new Dictionary<string, string> { { "name", "John Doe" }, { "age", "30" } };

// Stacks
Stack<int> myStack = new Stack<int>();
myStack.Push(1);
myStack.Push(2);
myStack.Pop(); // 2

// Queues
Queue<string> myQueue = new Queue<string>();
myQueue.Enqueue("Hello");
myQueue.Enqueue("World");
myQueue.Dequeue(); // Hello
```

## ADT

Sure, here are some of the methods that are available on the different types of collections in C#:

- **Arrays**

  - `Add(item)`: Adds an item to the end of the array.
  - `Remove(item)`: Removes an item from the array.
  - `Clear()`: Removes all items from the array.
  - `IndexOf(item)`: Returns the index of the first occurrence of an item in the array.
  - `Count()`: Returns the number of items in the array.
  - `ForEach(delegate)`: Executes a delegate for each item in the array.

- **Lists**

  - `Add(item)`: Adds an item to the end of the list.
  - `Remove(item)`: Removes an item from the list.
  - `Clear()`: Removes all items from the list.
  - `IndexOf(item)`: Returns the index of the first occurrence of an item in the list.
  - `Count()`: Returns the number of items in the list.
  - `ForEach(delegate)`: Executes a delegate for each item in the list.
  - `Insert(index, item)`: Inserts an item at a specified index in the list.
  - `RemoveAt(index)`: Removes an item at a specified index in the list.
  - `Sort()`: Sorts the list in ascending order.
  - `Reverse()`: Reverses the order of the items in the list.

- **Dictionaries**

  - `Add(key, value)`: Adds a key-value pair to the dictionary.
  - `Remove(key)`: Removes a key-value pair from the dictionary.
  - `Clear()`: Removes all key-value pairs from the dictionary.
  - `ContainsKey(key)`: Returns true if the dictionary contains a key.
  - `ContainsValue(value)`: Returns true if the dictionary contains a value.
  - `Get(key)`: Returns the value for a specified key.
  - `Keys()`: Returns an array of all the keys in the dictionary.
  - `Values()`: Returns an array of all the values in the dictionary.
  - `Count()`: Returns the number of key-value pairs in the dictionary.

- **Stacks**

  - `Push(item)`: Adds an item to the top of the stack.
  - `Pop()`: Removes an item from the top of the stack.
  - `Peek()`: Returns the item at the top of the stack without removing it.
  - `Clear()`: Removes all items from the stack.
  - `Count()`: Returns the number of items in the stack.

- **Queues**

  - `Enqueue(item)`: Adds an item to the end of the queue.
  - `Dequeue()`: Removes an item from the beginning of the queue.
  - `Peek()`: Returns the item at the beginning of the queue without removing it.
  - `Clear()`: Removes all items from the queue.
  - `Count()`: Returns the number of items in the queue.

Sure, here are some code snippets that demonstrate the different features of C#:

- **Enums**

  - Enums are a way of representing a set of named constants.
  - They are declared using the `enum` keyword.
  - For example:

```c#
enum DaysOfTheWeek
{
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday
}

// This code will print "Monday":
Console.WriteLine(DaysOfTheWeek.Monday);
```

- **Enumeration**

  - Enumeration is the process of creating a list of named constants.
  - Enums are often used to represent things like the days of the week, the months of the year, or the possible values of a Boolean flag.
  - Enums can be used to make code more readable and maintainable.

For example, let's say we want to create an enum to represent the different types of animals. We could do this like this:

```c#
enum AnimalType
{
    Dog,
    Cat,
    Bird,
    Fish
}
```

Now, we can use this enum to make our code more readable and maintainable. For example, let's say we have a function that takes an animal type as an argument. We could do this like this:

```c#
public void FeedAnimal(AnimalType animalType)
{
    switch (animalType)
    {
        case AnimalType.Dog:
            Console.WriteLine("Feeding the dog");
            break;
        case AnimalType.Cat:
            Console.WriteLine("Feeding the cat");
            break;
        case AnimalType.Bird:
            Console.WriteLine("Feeding the bird");
            break;
        case AnimalType.Fish:
            Console.WriteLine("Feeding the fish");
            break;
    }
}
```

This code is much more readable and maintainable than if we had to hard-code the different types of animals into the function.

- **Delegates**

  - Delegates are a way of representing a function pointer.
  - They are declared using the `delegate` keyword.
  - For example:

```c#
delegate void MyDelegate(string message);
```

This declaration creates a delegate type called `MyDelegate` that takes a single string argument and returns nothing.

We can use this delegate type to declare functions that accept a string argument and return nothing. For example:

```c#
public void PrintMessage(string message)
{
    Console.WriteLine(message);
}

// This function is declared as a delegate type:
public void MyDelegate(string message)
{
    PrintMessage(message);
}
```

We can also use delegates to pass functions as arguments to other functions. For example:

```c#
public void DoSomething(MyDelegate delegate)
{
    delegate("Hello, world!");
}

// This code will print "Hello, world!":
DoSomething(PrintMessage);
```

- **Callback Functions**

  - Callback functions are functions that are passed as arguments to other functions.
  - They are often used to handle events or to perform tasks asynchronously.
  - Callback functions can be declared using the `delegate` keyword, or they can be anonymous functions.

For example, let's say we have a function that displays a message to the user. We could do this like this:

```c#
public void DisplayMessage(string message)
{
    Console.WriteLine(message);
}
```

Now, we can use this function to display a message to the user when an event occurs. For example, let's say we have a button that the user can click. We could do this like this:

```c#
private void Button_Click(object sender, EventArgs e)
{
    // This code will display a message to the user:
    DisplayMessage("You clicked the button!");
}
```

In this example, the `DisplayMessage` function is a callback function. It is passed as an argument to the `Button_Click` event handler.

- **Arrow Functions**

  - Arrow functions are a new feature in C# 7 that allow you to write concise and expressive functions.
  - They are declared using the `=>` operator.
  - For example:

```c#
(x) => x * x; //
```

### Modifiers

- **Public**

  - The `public` access modifier is the most permissive. It allows access to the member from anywhere in the program.

For example:

```c#
public string Name { get; set; }
```

This declaration creates a public property called `Name` that can be accessed from anywhere in the program.

- **Internal**

  - The `internal` access modifier allows access to the member from anywhere in the assembly.

For example:

```c#
internal int Age { get; set; }
```

This declaration creates an internal property called `Age` that can be accessed from anywhere in the assembly.

- **Private**

  - The `private` access modifier only allows access to the member from the class in which it is declared.

For example:

```c#
private string Address { get; set; }
```

This declaration creates a private property called `Address` that can only be accessed from the class in which it is declared.

- **Protected**

  - The `protected` access modifier allows access to the member from the class in which it is declared, as well as from any derived classes.

For example:

```c#
protected string Phone { get; set; }
```

This declaration creates a protected property called `Phone` that can be accessed from the class in which it is declared, as well as from any derived classes.

- **Protected internal**

  - The `protected internal` access modifier allows access to the member from the class in which it is declared, as well as from any derived classes in the same assembly.

For example:

```c#
protected internal string Email { get; set; }
```

This declaration creates a protected internal property called `Email` that can be accessed from the class in which it is declared, as well as from any derived classes in the same assembly.

- **Friend**

  - The `friend` access modifier allows access to the member from any class that is declared as a friend of the class in which the member is declared.

For example:

```c#
friend class MyFriendClass;

string FriendProperty { get; set; }
```

This declaration creates a public property called `FriendProperty` that can only be accessed from the class `MyFriendClass`.

- **No modifier**

  - If no access modifier is specified, the member is private by default.

For example:

```c#
string Name;
```

This declaration creates a private property called `Name` that can only be accessed from the class in which it is declared.
