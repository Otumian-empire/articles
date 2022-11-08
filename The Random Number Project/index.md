# Distribution of Random Numbers

So, Distribution of Random Numbers in `C`!! Let's dive in.

I believe that at least you have heard of _Mean_, _Median_ and _Mode_. They aren't comedians as their names might suggest. If you have't then Mean is <!-- define what mean is and provide and link to it, do the same for median and mode-->.

We are basically interested in some random number distributions and we would use the random module for that so that we don't have to think about writing such functionality (I was not even thinking of doing something like that).

We want values that fit between 0 and 10 (0 included, 10 excluded).

```C
random_number = (int) (10.0*rand()/(RAND_MAX + 1.0));
```

The `C` snippet above summarizes the random values we need but, we'd do things in python (you know, it comes with less and tolerable headache).

We'd implement some functions for Mean, Frequency, Serial and another called Poker (distribution/test).

<!-- What to expect from this article -->

## Distribution and Description

- **Mean**: Calculate the mean of 1000 random numbers. The result should be close to 4.5.
- **Frequency**: Tabulate the percentage of each digit (0 throughout 9) in 10,000 generated numbers. Each Is expected to be close (roughly) to 10%.
- **Serial**: Generate 10,000 pairs of numbers. Tabulate the frequency of each pair, 00, 01,02, ….., 99. This time we would expect roughly 1% in each category.
- **Poker**: Generate four digits at a time, and repeat 1,000 times (a thousand sets of 4 digits). Tabulate the sets as: i) all the same (e.g. 4444), ii) 3 digits the same (e.g. 4443, 3444 or 4344), iii) two pairs (e.g. 4334, 4433), iv) one pair (e.g. 4324 or4342), or v) none identical. In theory we would expect frequencies of 1, 36, 27, 432 & 504 respectively for a thousand sets of numbers (i.e., 4,000 digits). You will not necessarily get those exact numbers.
- **Poker, using a file**: Generate 4,000 random digits and save them in a text file (using ASCII coding), where characters are separated by spaces. Repeat the poker test by reading the numbers from the file.
