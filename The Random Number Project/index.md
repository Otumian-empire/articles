# Distribution of Random Numbers

So, Distribution of Random Numbers in `C`!! Let's dive in.

I believe that at least you have heard of _Mean_, _Median_ and _Mode_. They aren't comedians as their names might suggest. If you haven't then read about them here: [Mean][Wiki-mean], [Mode][Wiki-mode], and [Median][Wiki-median].

We are interested in some random number distributions and we would use the random module for that so that we don't have to think about writing such functionality (I was not even thinking of doing something like that).

We want values that fit between 0 and 10 (0 included, 10 excluded).

```C
random_number = (int) (10.0*rand()/(RAND_MAX + 1.0));
```

The `C` snippet above summarizes the random values we need but, we'd do things in Python in the next article (you know, it comes with less and tolerable headaches).

We'd implement some functions for Mean, Frequency, Serial and another called Poker (distribution/test).

<!-- What to expect from this article -->

## Distribution and Description

- **Mean**: Calculate the mean of 1000 random numbers. The result should be close to 4.5.
- **Frequency**: Tabulate the percentage of each digit (0 throughout 9) in 10,000 generated numbers. Each Is expected to be close (roughly) to 10%.
- **Serial**: Generate 10,000 pairs of numbers. Tabulate the frequency of each pair, 00, 01, 02, ….., 99. This time we would expect roughly 1% in each category.
- **Poker**: Generate four digits at a time, and repeat 1,000 times (a thousand sets of 4 digits). Tabulate the sets as:

  - all the same (e.g. 4444)
  - 3 digits the same (e.g. 4443, 3444 or 4344)
  - two pairs (e.g. 4334, 4433)
  - one pair (e.g. 4324 or4342)
  - none identical

  In theory, we would expect frequencies of 1, 36, 27, 432 & 504 respectively for a thousand sets of numbers (i.e., 4,000 digits). You will not necessarily get those exact numbers.

- **Poker, using a file**: Generate 4,000 random digits and save them in a text file (using ASCII coding), where characters are separated by spaces. Repeat the poker test by reading the numbers from the file.

## Implementation

Let's get ready for some headaches 🫡!!

### Imports

We will make use of the `stdio` and `stdlib` libraries for `I/O` operations and for the random number generation, respectively.

```C
#include <stdio.h>
#include <stdlib.h>
```

### Constants

We shall define constants for each of the tests for each of the distributions. We have mean, frequency, serial and poker tests.

```C
// constants for each test (options)
#define MEAN_TEST 1
#define FREQUENCY_TEST 2
#define SERIAL_TEST 3
#define POKER_TEST 4
#define POKER_TEST_FILE 5
```

Booleans for in `C` are `1`s and `0`s. However, to make it easy for the brain (mental mapping), we defined constants for this.

```C
// constants for TRUE and FALSE
#define TRUE 1
#define FALSE 0
```

In the last test, the poker test, we'd also do one where we read the dataset from a file.

```C
// constant for reading and writing to file
// filename - poker.txt
#define POKER_TEST_FILENAME "poker.txt"
#define WRITE_MODE "w"
#define READ_MODE "r"
```

Values will be passed via the CLI and we have to know the number of values we pass.

```C
// argument count - user must pass a test option
// which indicates which test to run this increases
// argc to 2 (including the program filename)
const int argumentCount = 2;
```

### Functions and Procedures

We need a way to prompt the user however, we don't want to repeat the same prompt all the time.

```C
// prompt user to enter an option (number) indicating a test
// to run when no option is passed when running the program
void promptUser()
{
    printf("Pass 1, 2, 3 or 4 to run Mean, Frequency, ");
    printf("Serial or Poker Test respectively.\n");
}
```

Initially, we showed that we can generate the random numbers using the snippet:

```C
(int)(10.0 * rand() / (RAND_MAX + 1.0))
```

To make it easier to use, we make it into a `void` function.

```C
// returns a random number
int genRand()
{
    return (int)(10.0 * rand() / (RAND_MAX + 1.0));
}
```

In the poker test:

- all the same (e.g. 4444)
  ```C
  // compare all 4 digits to be equal
  // (return 1 for true and 0 for false)
  int hasFourDigitsEqual(int a, int b, int c, int d)
  {
        return (a == b && b == c && c == d) ? TRUE : FALSE;
  }
  ```
- 3 digits the same (e.g. 4443, 3444 or 4344)

  ```C
  // compare all 4 digits, for 3 equal digits to be equal
  // (return 1 for true and 0 for false)
  int hasThreeDigitsEqual(int a, int b, int c, int d)
  {
        if (a == b && b == c)
            return TRUE;

        else if (a == b && b == d)
            return TRUE;

        else if (a == c && c == d)
            return TRUE;

        else if (b == c && c == d)
            return TRUE;

        return FALSE;
  }
  ```

- two pairs (e.g. 4334, 4433)

  ```C
  // compare all 4 digits, for 2 pairs repeated
  // (return 1 for true and 0 for false)
  // NB: 2222 will pass but will fail in this case
  // because of the arrangement of the if and else statements
  int hasTwoPairDigitsEqual(int a, int b, int c, int d)
  {
      if (a == b && c == d)
          return TRUE;

      else if (a == c && b == d)
          return TRUE;

      else if (a == d && b == c)
          return TRUE;

      return FALSE;
  }
  ```

- one pair (e.g. 4324 or4342)

  ```C
  // compare all 4 digits, for 1 pair repeated
  // (return 1 for true and 0 for false)
  int hasOnePairDigitsEqual(int a, int b, int c, int d)
  {
      if (a == b)
          return TRUE;

      else if (a == c)
          return TRUE;

      else if (a == d)
          return TRUE;

      else if (b == c)
          return TRUE;

      else if (b == d)
          return TRUE;

      else if (c == d)
          return TRUE;

      return FALSE;
  }
  ```

- none identical: we can combine the others

### The Distribution Tests

- Mean Test

  ```C
  // prints the mean of 1000 trials
  void meanTest()
  {
      const int rounds = 1000;
      float mean = 0;

      for (int i = 0; i < rounds; i++)
      {
          mean += genRand();
      }

      mean /= rounds;

      printf("Mean Test of %i\n", rounds);
      printf("Mean = %.1f\n", mean);
  }
  ```

- Frequency Test

  ```C
  // prints a table of percentages for 10000 trials for value [0, 9]
  void frequencyTest()
  {
      const int rounds = 10000;
      const int range = 10;
      const float totalPercentage = 100.0;
      int frequency[10] = {0};

      for (int i = 0; i < rounds; i++)
      {
          frequency[genRand()] += 1;
      }

      printf("Frequency Test of %i\n\n", rounds);

      printf("%-2c| %-3c\n", 'X', '%');
      printf("--------\n");

      for (int i = 0; i < range; i++)
      {
          printf("%-2i| %-3.2f\n", i, (float)frequency[i] / totalPercentage);
      }
  }
  ```

- Serial Test

  ```C
  // prints a table of percentages for 10000 trials for
  // pairs of values [00, 99]
  void serialTest()
  {
      const int rounds = 10000;
      const int range = 10;
      const float totalPercentage = 100.0;
      int frequency[10][10] = {0};

      for (int i = 0; i < rounds; i++)
      {
          frequency[genRand()][genRand()] += 1;
      }

      printf("Serial Test of %i\n\n", rounds);

      printf("%c%-2c| %-3c\n", 'X', 'Y', '%');
      printf("---------\n");

      for (int i = 0; i < range; i++)
      {
          for (int j = 0; j < range; j++)
          {
              printf("%i%-2i| %-3.2f\n", i, j,
                  (float)frequency[i][j] / totalPercentage);
          }
      }
  }
  ```

- Poker Test

  ```C
  // prints tables of 4-digit values of different classes
  // classes:
  //     all_the_same -> all 4 digits are the same (repeated 4)
  //     three_the_same -> 3 of 4 are the same (repeated 3)
  //     two_pair -> 2 pairs of 4 are the same (2, 2 repeated)
  //     one_pair -> 2 of 4 are the same (1, 2 repeated)
  //     none_identical -> all 4 are different (no repeat)
  void pokerTest()
  {
      const int rounds = 1000;

      // if same class, add to the same class
      // else if trio class, add to the trio class
      // else if duo class, add to the duo class
      // else if mono class, add to the mono class
      // else add to the unique class

      int digit_1 = 0, digit_2 = 0, digit_3 = 0, digit_4 = 0;
      int all_the_same = 0, three_the_same = 0, two_pair = 0;
      int one_pair = 0, none_identical = 0;

      // generate 4 random numbers, 1000 times (hold 1000 trials)
      for (int i = 0; i < rounds; i++)
      {
          // get the random numbers to compare them
          digit_1 = genRand();
          digit_2 = genRand();
          digit_3 = genRand();
          digit_4 = genRand();

          if (hasFourDigitsEqual(digit_1, digit_2, digit_3, digit_4))
          {
              all_the_same += 1;
          }
          else if (hasThreeDigitsEqual(digit_1, digit_2, digit_3, digit_4))
          {
              three_the_same += 1;
          }
          else if (hasTwoPairDigitsEqual(digit_1, digit_2, digit_3, digit_4))
          {
              two_pair += 1;
          }
          else if (hasOnePairDigitsEqual(digit_1, digit_2, digit_3, digit_4))
          {
              one_pair += 1;
          }
          else
          {
              none_identical += 1;
          }
      }

      printf("Poker Test of %i\n\n", rounds);

      printf("number of digits  | %-3c\n", '%');
      printf("-----------------------\n");
      printf("%-18s| %i\n", "all the same", all_the_same);
      printf("%-18s| %i\n", "3 digits the same", three_the_same);
      printf("%-18s| %i\n", "two pairs", two_pair);
      printf("%-18s| %i\n", "one pairs", one_pair);
      printf("%-18s| %i\n", "none identical", none_identical);
  }
  ```

- Poker Test From a File

  ```C
  // poker test - reading digits from file
  void pokerTestFile()
  {
      const int rounds = 4000;

      // file pointer
      FILE *fp;

      // Write 4000 random numbers into POKER_TEST_FILENAME
      fp = fopen(POKER_TEST_FILENAME, WRITE_MODE);

      for (int i = 0; i < rounds; i++)
      {
          fprintf(fp, "%i ", genRand());
      }

      // open the file for reading and read its content
      fp = fopen(POKER_TEST_FILENAME, READ_MODE);

      int digit_1 = 0, digit_2 = 0, digit_3 = 0, digit_4 = 0;
      int all_the_same = 0, three_the_same = 0, two_pair = 0;
      int one_pair = 0, none_identical = 0;

      // Moves the file position indicator to the beginning of the
      //  given file stream.
      rewind(fp);

      for (int i = 0; i < rounds; i++)
      {
          // read file content in the same manner as written
          fscanf(fp, "%i %i %i %i ", &digit_1, &digit_2, &digit_3, &digit_4);

          if (hasFourDigitsEqual(digit_1, digit_2, digit_3, digit_4))
          {
              all_the_same += 1;
          }
          else if (hasThreeDigitsEqual(digit_1, digit_2, digit_3, digit_4))
          {
              three_the_same += 1;
          }
          else if (hasTwoPairDigitsEqual(digit_1, digit_2, digit_3, digit_4))
          {
              two_pair += 1;
          }
          else if (hasOnePairDigitsEqual(digit_1, digit_2, digit_3, digit_4))
          {
              one_pair += 1;
          }
          else
          {
              none_identical += 1;
          }
      }

      fclose(fp);

      printf("Poker Test of %i random numbers from file\n\n", 4 * rounds);

      printf("number of digits  | %-3c\n", '%');
      printf("-----------------------\n");
      printf("%-18s| %i\n", "all the same", all_the_same);
      printf("%-18s| %i\n", "3 digits the same", three_the_same);
      printf("%-18s| %i\n", "two pairs", two_pair);
      printf("%-18s| %i\n", "one pairs", one_pair);
      printf("%-18s| %i\n", "none identical", none_identical);
  }
  ```

### Main function

This is the entry point for the program. We are to make sure that the argument passed counts to 2. If not, we prompt the user to enter a test.

```C

int main(int argc, char const *argv[])
{

    if (argc != argumentCount)
    {
        promptUser();
    }
    else
    {
        // get the test option passed by the user from argv[1]
        int testOption;
        sscanf(argv[1], "%d", &testOption);

        switch (testOption)
        {
        case MEAN_TEST:
            meanTest();
            break;

        case FREQUENCY_TEST:
            frequencyTest();
            break;

        case SERIAL_TEST:
            serialTest();
            break;

        case POKER_TEST:
            pokerTest();
            break;

        case POKER_TEST_FILE:
            pokerTestFile();
            break;

        default:
            printf("Test Not Known\n");
            promptUser();
            break;
        }
    }

    return 0;
}
```

### Compile and run

- Compile, `gcc file_name.c -o app`
- Run, `./app <TEST_TO_RUN>`
- MEAN_TEST = 1, FREQUENCY_TEST = 2, SERIAL_TEST = 3, POKER_TEST = 4

### Others

These are other files you'd need:

- Poker test with a text file, [poker-test-file]
- Makefile, [makefile-file]

## Conclusion

We implemented the functions for Mean, Frequency, Serial and Poker distributions. Defined constants to reduce the use of literals, which also makes it easier to mentally map variables (names) to the value they hold. There were a lot of instances where we could simplify some functions, however, that was not the purpose. The objective was to generate random values and test them against the distribution description we had from the start.

## Source

- [Mean][Wiki-mean]
- [Mode][Wiki-mode]
- [Median][Wiki-median]
- [Procedure vs Function][procedure-function]

#

[Wiki-mean]: https://en.wikipedia.org/wiki/Mean
[Wiki-median]: https://en.wikipedia.org/wiki/Median
[Wiki-mode]: https://en.wikipedia.org/wiki/Mode_(statistics)
[procedure-function]: https://stackoverflow.com/a/721107
[poker-test-file]: https://gist.github.com/Otumian-empire/f4dc8be0251e2bcf3e24dd478014435e
[makefile-file]: https://gist.github.com/Otumian-empire/37cce79db68c604b7014511bdb838589
