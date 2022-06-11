# Why should you use python to solve algorithm problems?

First let us start with a problem. The first time I read the question, I didn't understand. I couldn't make sense out of the question, even after reading it several times. In most algo questions, there are sample input and output. I dived into it. I tried to find a pattern in the sample input and output.

## So the problem in brief.

Given `N` wheels to spin `X` times, where spinned will will may point to a value in the range between 1 and 9 inclusive. Find the sum of all the maximum values in each spin (This is even wrong but close).

Does it make sense or give you a gist of how to approach the problem? To me, No..

## Sample input and output

```py
arr = ["123", "642", "925", "376"]
```

From this, the number of wheels is 4 and it was spinned 3 times (Have you seen N and X?).

To save me the time and effort, let's call each `Wx` where `x=1,2,3,4`.

> let -> mean, pointed to

In the first spin: _W1 -> 1, W2 -> 6, W3 -> 9 and W4 -> 3_

In the second spin: _W1 -> 2, W2 -> 4, W3 -> 2 and W4 -> 7_

In the third spin: _W1 -> 3, W2 -> 2, W3 -> 5 and W4 -> 6_

## IO flow

Let me show you something or how I was able to understand what the whole problem is:

```
1 2 3
6 4 2
9 2 5
3 7 6
```

**9** will be picked in _W3_ then 3, 6 and 7 will be dropped from the _W1_, _W2_ and _W4_ respectively

```
1 2
4 2
2 5
3 6
```

**6** will be picked in _W4_ then 2, 4 and 5 will be dropped from the _W1_, _W2_ and _W3_ respectively

```
1
2
2
3
```

**3** will be picked in _W4_ then 1, 2 and 2 will be dropped from the _W1_, _W2_ and _W3_ respectively

The sum of the picked value will be `9 + 6 + 3 = 18`

## How weird?

There was two ways that dropped in my head but the second one came when I started to think in python. Using the knowledge from lists and its indexing.

First remember, the values in the array (list in python) are all strings and before we can do anything with those value we have to convert each of them to an integer.

This was like, find the maximum value from each row, and then find the max from those maximum values. This way either we have to remove the maximum values from each row or we have to create new list for the maximum values a whole lot of thinking to an extent, 30 minutes I was staring at the screen (what was I doing again, I was lost in thought)

The algo I used after I walked about and hydrated..

## Algo:

- Convert each string into an array where each character is converted into an integer. Something like, `"123"` becomes, `[1,2,3]`
  so the sample input changes in the program.

  ```py
  arr = ["123", "642", "925", "376"]
  int_arr = [[1, 2, 3], [6, 4, 2], [9, 2, 5], [3, 7, 6]]
  ```

  > This is called a nested list

- Now sort the arrays inside the int_arr
  ```py
  sorted_int_arr = [[1, 2, 3], [2, 4, 6], [2, 5, 9], [3, 6, 7]]
  ```
- Using two loops (because the values I want are inside another array.
  So we will use the inner loop to get access to each array in side the mother array and then use the outer array to point the elements in each column.

  ```py
  max_sum = 0
  max_arr = []

  for i = 0 to X:
  	for j = 0 to N:
  	sorted_int_arr[j][i] -> the element in each row
  	so if i = 0, j = 0, sorted_int_arr[j][i] = 1
  	if i = 0, j = 1, sorted_int_arr[j][i] = 2
  	if i = 0, j = 2, sorted_int_arr[j][i] = 2
  	if i = 0, j = 3, sorted_int_arr[j][i] = 3
  	we could read this values into another array, say max_array
  	max_arr = [1,2,2,3]
  	get the max of max_arr, max(max_arr) -> 3
  	add max(max_arr) -> 3 to max_sum
  	i increase

  		repeat these processes and you would finally come to a stop when the mother loop terminates
  ```

The difference here is that, it will be as if we are working backwards, which is true.

## The full pythonic code

```py

# returns the sum of the maximum number in each column

n = 4
spin = ['137', '364', '115', '724']
ans = 14

def spin_mac(n, spin):
	ans = 0
	row_count = len(spin[0])

    sorted_spin = [sorted([int(entry) for entry in row]) for row in spin]

    for count in range(row_count):
        ans += max([row[count] for row in sorted_spin])

    return ans

print(ans == spin_mac(n, spin))

```
