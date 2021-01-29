# How long does it take to learn Fortran

The deal was to work on a project for one senior student. It was rumoured that I knew Fortran. The sad truth was that I didn't. I was bored and I was only goofing with forth, not Fortran. Who makes such a deliberate mistake. The money was promising to why not spend a few hours on a new language I have not used before. What do programmers do? They learn and adapt. Within six hours, I was taken notes on Fortran and this is the note.

## 1 - Basics

- comment

  ```Fortran
  ! - starts a comment
  ```

- start and end of a program
  Every code must have a program name and `end` program name, as in

  ```Fortran
  program HelloWorld
  ! code here

  end HelloWorld
  ```

- `implicit none` - checks if all variables are declared

- variable declaration
  `type :: var`

  as in , `real :: x, y` and `integer :: age, numberOfDays`

- output and input
  ```Fortran
    print _, objects
    read _, objects
  ```
- sample code
  we can do,

  ```Fortran
  program simplecode
  ! This program demonstrates what we have seen so far

  integer :: a, b, c

  print _, "Enter a:"
  read _, a

  print _, "Enter a:"
  read _, a

  c = a+b

  print \*, c

  end program simplecode
  ```

- It is considered that every file must have one program

  ```Fortran
  ! character data type.
  ! this is most similar to c
  ! in c,
  ! char name[10];
  ! in Fortran,
  character :: name\*10
  ```

## 2 - Making Decisions

- `var = val`, is a simple assigment statement

- operators: `+, -, \*, /, \*\*, (), mod`

- intrinsic functions are builtin functions such as `sin, cos, exp, tan, atan, log, mod, ...`

- `==`, checks for equality, like in C

- if statement follows the patterns

  ```Fortran
  if (condition) then code end if
  ```

- sample

  ```Fortran
  program sampleIf
  integer :: age
  read _, age

  if (age == 10) then
  print_, 'you are ten'
  end if

  end program sampleIf
  ```

- A good program:

  - Uses comments appropriately to explain what is happening.
  - Uses indentation to make the program easier to read.
  - Uses meaningful variable names.
  - Uses sensible prompts to let the user know what is going on.
  - Uses implicit none at the start of every program.
  - Is efficient!

- if then, else if then and else and end if

  ```Fortran
  program sampleIfElse
  implicit none
  integer :: num
  print*, 'enter num'
  read *, num

  if (num == 10) then
  num = num - 2
  else if (num == 9) then
  num = num - 3
  else
  num = 0
  end if

  print \*, num

  end program sampleIf
  ```

- relation operators:` ==, /=, <, >, <=, >=`
- logical operators: `.and., .or.`
- stop - literally stops the program

  ```Fortran
  if (condition) stop
  ```

- there is a difference in a real zero and an integer zero,
  as such you should find the absolute value of the real of interest,
  check if its less than some arbitrary number, say, 0.000001

## 3 - Loops

- integer division does not result in a real result

- `do-loop` allows re-execution of codes, just like a `for-loop` in c

- do-loop is of the form
  ```Fortran
  do var = begin, end, step
    ! code
  end do
  ```
- The do loop is a `start` and `end` inclusive unlike c whereby, `0 to 20` is `0 to 19`

- Nested loops
  ```Fortran
  do var_i=a,b,c
    do var_j=d,e,f
      ! code
    end do
  end do
  ```

## 4 Using Files and Extending Precision

- use `open` to open a file. `open` takes two args, a positional arg and kwarg. These are unit/input device, an `int` value and file name as `file=fileName`

- `read _, someVar`, reads data into `someVar` but has to be modified to read from a file.
- `read(device, _) someVars `, there is no comma after the closing bracket
- sample code

  ```Fortran
  program readIntFromFile
  ! create a file, data.txt and write a number into
  ! it, save it

    implicit none

    integer :: i
    open(1, file='data.txt')
    read(1, *) i

    print*, i

  end program readCharFromFile
  ```

- `open` links the `file` to be read with an input device numbered, `1`
- `write` behave like `read`, so just in the above code, change `read` to `write` to write to file
- sample code

  ```Fortran
  program writeToFile
  ! create a file, data.txt and enter a number into it, save it

    implicit none

    integer :: i
    open(1, file='data.txt')
    read(1, *) i

    print*, i

  end program writeToFile
  ```

- By default the precisions of `integer` and `real` is `6dp` but can be extended
- This is almost the same concept around `typdef` - creating a new data type
- `type, parameter :: typeKind=selected_real_kind(p=val)`

- To make a type of the new data type, `type (kind=newDataType) :: var_name`

- One other way is to append the new type as `val_newDataType` as in `1.34_newDataType`

## 5 Arrays and Formatted I/O

- An array is a list that we can access through a subscript
- we use the size of the array when we declare it.
- As in, `real, dimension(100) :: arr`, creates an array, `arr` of size `100`

- subscripting, `arr(index)`, where the array index starts from `1`, unlike c, which is `0`
- `print *, array`, prints the content of the array

- sample code

  ```Fortran
  program arrays
  implicit none

    ! declare an array of size, 10
    integer, dimension(10) :: intArray

    ! populate the array, using a loop
    integer :: i
    do i = 1, 10
        intArray(i) = i
    end do

    print *, intArray

  end program
  ```

- To make the code above maintainable we can create a simple variable to hold the size of the array. This a parameter of the array.

  ```Fortran
  integer, parameter :: arraySize = 10
  integer, dimension(arraySize) :: intArray
  ```

- arraySize could even be passed into the loop

- Arrays can be created at run time as wells, whereby the size of the array is created when the user passes the size

- make use of the `arrayVar allocatable`, here the dimension is set to,` dimension(:)`
- allocate the size of the array when taken from the user
- `deallocate` the array - something like free space

- sample code

  ```Fortran
  program runTimeArray
  implicit none

    ! declare the array, allocatable with  dimension(:)
    integer, allocatable, dimension(:) :: arr

    integer :: arraySize

    ! loop var
    integer :: i

    ! read/determin array size
    print *, 'enter array size'
    read *, arraySize

    ! allocate memory of arraySize to array
    allocate(arr(arraySize))

    ! populate the array

    do i = 1, arraySize
        arr(i) = i ** 2
    end do

    ! print arr
    print*, arr

    ! release memory
    deallocate(arr)

  end program
  ```

- operations can easily be done on every arrays element by using simple arithmetic operators and intrinsic functions

- `integer, dimension(2, 2) :: twoDimenArr` creates a 2D array with 4 components that supports `twoDimenArr(1,1)` indexing

## 6 Subroutines and Functions

- A `subroutine/function` here is the basic idea of that in C.
- Instead of `program programName` and `end program`, for `subroutine`, we do,` subroutine subroutineName` and `end subroutine`
- We do, call `subroutineName` to call the subroutine.

- Consider the program below.

  ```Fortran
    program subroutineProgram
    implicit none

        call sayHello()

    end program

    subroutine sayHello( )
    print \*, 'Hello'
    end subroutine
  ```

### Some notes

- several subroutines may be created in a single program.
- ideally, a subroutine should do a specific task – reflected by its name.
- all the variables in subroutines, apart from the ones passed as arguments, are 'hidden' from the main program.
- it is very easy to forget to declare variables in subroutines, thus use implicit none.
- all the variables in the subroutine must be declared.
- the positioning of the arguments is important. The subroutine has no knowledge of what the variables are called in the main program.
- it is vital that the arguments agree both in position and type.

### functions

A function is just like a subroutine but returns a value

```Fortran
function rads(degrees)
implicit none
integer, parameter :: ikind=selected_real_kind(p=15)

    ! returns radians
    real (kind=ikind) :: pi, degrees, rads

    pi= 4.0_ikind * atan(1.0_ikind)

    rads=(degrees*pi/180.0_ikind)

end function rads
```

Uses the above-created function

```Fortran
program func
! demonstrates the use of user-defined functions
implicit none

    integer, parameter :: ikind=selected_real_kind(p=15)
    real (kind=ikind):: deg, rads

    print *, 'Enter an angle in degrees'
    read *, deg

    write(*,10) 'sin = ',sin(rads(deg))
    write(*,10) 'tan = ',tan(rads(deg))
    write(*,10) 'cos = ',cos(rads(deg))

    10 format(a,f10.8)

end program func
```

## Some notes

- everything about subroutines applies to functions
- the function `rads` converts the value of the argument, degrees, to radians.
- declare the data type of the function both in the main program and in the function itself as if it were a variable.
- functions return one value. This value, when calculated, is assigned to the name of the function as if it were a variable – `rads = (degrees * pi / 180.0_ikind)`
