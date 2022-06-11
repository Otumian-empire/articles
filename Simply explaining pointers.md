# Simply explaining a pointer

A pointer is a variable that contains the address of another variable. Basically saying that a pointer is a variable that points to the memory location of another variable and can change the value at that address indirectly.

## Making sense of value and memory address

Two facts we know or have to know to set things straight:

- `&` for the address and
- `*` for the value at an address.

Let's say we have `int num = 3;` We assign the value `3` to the variable `num`.

So to print out the value of `num`:

```c
printf("value of num: %d\n", num);
/* value of num: 3 */
```

How do we then get the address of `num`? Remember the `&`? We precede the variable with `&`.

```c
printf("address of num: %p\n", &num);
/* address of num: 0x7ffe5faa05cc */
```

So now we have an address, how do we then get the value at that address? Remember the second fact, about `*`? Precede the memory address with a `*`. We got the address by `&num` and by preceding the address, `&num`, by `*`, as `*(&num)`, we would get the value at that address.

```c
printf("value at address of num: %d\n", *(&num));
/* value at address of num: 3 */
```

### Takeaways

So what we have been able to deduce is:

- `int num = 3;` means `num` has a value of `3`.
- `&num` returns the memory address of `num`.
- `*(&num)` returns the value at the memory address, `&num`, of `num`.

### Final script

```c
#include <stdio.h>

int main() {
    int num = 3;

    printf("value of num: %d\n", num);
    printf("address of num: %p\n", &num);
    printf("value at address of num: %d\n", *(&num));

    return 0;
}

```

## Delving into pointers

Creating a pointer is simple. It is basically as declaring or initializing a variable - well a pointer is a variable. Consider the snippet below as to how to create a pointer.

```c
// NOTE: int is used for the sake of simplicity

// case 1 - initialize a pointer
int *ptr = &var;

// case 2 - declare and define later
// ptr should be initialized to NULL
// until it is assigned a valid location
// int *ptr1;
int *ptr1 = NULL;
ptr = &var;

```

Now let's get down to pointer business. Say we have `num` assigned the value of `3`, just as we have done before. We shall create a pointer to `num`.

```c
int num = 3;
int *ptr = &num;

```

I have a question for you? You better play with the code to understand better.

### Question

_Which is the pointer? `*`, `ptr` or `*ptr`?_

### My answer

Well, I hope you gave it some thought.

- `*` is not the pointer. Remember the second fact. Given an address, `*` returns that value at that memory address.
- `*ptr` is the value at the memory address, `&num` - `num`.As such is not the pointer.
- `ptr` is the pointer. This is so because it has the memory address of `num` as value.

> I will encourage you to take a break, clear your head and read again or proceed.

### Pointer value and address

How do we get the value of a pointer? Don't get confused about the value of a pointer and what value the pointer points to. Try to understand the two before moving on. Something more or less like, the value of a pointer and the value at a pointer - what the pointer points to.

```c
printf("value of ptr: %p\n", ptr);
/* value of ptr: 0x7ffe5faa05cc */

```

How do we get the value at the pointer? Now the pointer, `ptr` is the same as `&num`. As such the value at the pointer (memory address) - `&num`, is `*(&num)`. `*ptr == *(&num)`.

```c
printf("value at ptr: %d\n", *ptr);
/* value at ptr: 3 */

```

The pointer, `ptr`, has its own address. How do we get the address of a pointer? This is a familiar question. Precede the variable with `&`.

```c
printf("address of ptr: %p\n", &ptr);
/* address of ptr: 0x7ffe5faa05d0 */

```

### Take away

- In `int *ptr = &num`, `ptr` is the pointer.
- `ptr` should be assigned `NULL` until given a location.
- `ptr` is the same as `&num` as such `*ptr`, `*(&num)` is the same as `num`.
- The pointer has its own address, `&ptr`.

### Final script

```c
#include <stdio.h>

int main() {
    int num = 3;
    printf("value of num: %d\n", num);
    printf("address of num: %p\n", &num);
    printf("value at address of num: %d\n", *(&num));

    int *ptr = &num;
    printf("value of ptr: %p\n", ptr);
    printf("value at ptr: %d\n", *ptr);
    printf("address of ptr: %p\n", &ptr);

    return 0;
}

```

## Source

- [sololearn c][sololearn-c]
- [21:everything u need 2 know about pointers -richard buckland][cs1 highercomputing - richard buckland unsw ]

#

[sololearn-c]: https://www.sololearn.com/Play/C
[cs1 highercomputing - richard buckland unsw ]: https://www.youtube.com/watch?v=Rxvv9krECNw&list=PL6B940F08B9773B9F&index=25
