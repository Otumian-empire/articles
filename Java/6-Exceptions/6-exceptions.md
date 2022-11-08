# Exceptions

An Exception occurs when a program is running and when they occur, the program that is being executed stops abruptly.

In programming the process of preventing such abruption is known as exception handling. With this you can something about your program when an exception occurs just like in an if or else statement.

There are several ways that an exception can occur and some of these are:

- invalid input
- accessing unavailable resource

Exceptions can be handled using the try and catch block. What ever block you want to execute will be in the try block and in the catch block you'd specify exceptions that would occur. This is similar to having expectations.

A simple try and catch block looks the the snippet below:
try{
// what ever
} catch (Exception e) {
// do something as the exception has occurred
}

we can manually generate exceptions. THis is like triggering it. YOu have a button and you want the user to click it for some functionality. It testing you have to trigger a button click since the automating is done by "R-O-B-O-T-S". We can achieve that by using the throw keyword

Let's do something similar

int input = 4;

if (input < 4) {
throw new Exception("Input is less than 4");
} else {
// do something
}

Sometimes, when instead of using try-and-catch, we can use the throws keyword. WIth the throws keyword, we try to tell whoever uses our method that there is a likelihood of an exception occurring as such take care of it.

int div(int a, int b) throws Exception {

    if (a < 4) {
        throw new Exception("'a' is less than 4");
    }

    return a / b;

}

Seriously we can do something like

int div(int a, int b) throws Exception {
return a / b;
}

Now, we know we can divide any number by '0', which mean there would be an exception. we can use the try and catch to handle that exception and print some nice response or return 0 or -1 to indicate things didn't go well. With the throws we focus on what we want to do and leave the handling of the potential exception to the user of the method.

we can handle several exceptions at the same time (In the same program). We put in several catch blocks. THis way may be able to handle different exceptions differently.

It will be okay now if we know about the exception tree.

- Throwable
  - Error
    - StackOverflowError
    - VirtualMachineError
    - OutOfMemoryError
  - Exception
    - IOException
    - SQLException
    - ClassNotFoundException
    - RuntimeException
      - ArithmeticException
      - NullPointerException
      - NumberFormatException
      - IndexOutOfBoundsException
        - ArrayIndexOutOfBoundsException
        - StringIndexOutOfBoundsException

https://www.javatpoint.com/exception-handling-in-java
