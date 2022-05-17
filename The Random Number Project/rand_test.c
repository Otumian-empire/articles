#include <stdio.h>
#include <stdlib.h>

// constants for each test (options)
#define MEAN_TEST 1
#define FREQUENCY_TEST 2
#define SERIAL_TEST 3
#define POKER_TEST 4
#define POKER_TEST_FILE 5

// constants for TRUE and FALSE
#define TRUE 1
#define FALSE 0

// constant for reading and writing to file
// filename - poker.txt
#define POKER_TEST_FILENAME "poker.txt"
#define WRITE_MODE "w"
#define READ_MODE "r"

// argument count - user must pass a test option
// which indicates which test to run this increases
// argc to 2 (including the program filename)
const int argumentCount = 2;

// prompt user to enter an option (number) indicating a test
// to run when no option is passed when running the program
void promptUser()
{
    printf("Pass 1, 2, 3 or 4 to run Mean, Frequency, ");
    printf("Serial or Poker Test respectively.\n");
}

// returns a random number
int genRand()
{
    return (int)(10.0 * rand() / (RAND_MAX + 1.0));
}

// compare all 4 digits to be equal
// (return 1 for true and 0 for false)
int hasFourDigitsEqual(int a, int b, int c, int d)
{
    return (a == b && b == c && c == d) ? TRUE : FALSE;
}

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

// prints a table percentages for 10000 trials for value [0, 9]
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

// prints a table percentages for 10000 trials for
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

    // if same class, add to same class
    // else if trio class, add to trio class
    // else if duo class, add to duo class
    // else if mono class, add to mono class
    // else add to unique class

    int digit_1 = 0, digit_2 = 0, digit_3 = 0, digit_4 = 0;
    int all_the_same = 0, three_the_same = 0, two_pair = 0;
    int one_pair = 0, none_identical = 0;

    // generate 4 randon numbers, 1000 times (hold 1000 trials)
    for (int i = 0; i < rounds; i++)
    {
        // get the random numbers to compair them
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

    // open file for reading and read the file content
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