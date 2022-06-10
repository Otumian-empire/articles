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
