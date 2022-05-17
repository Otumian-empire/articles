# [Lists](#top)

<div id="top"/>
In this session, we will discuss:

-   [ArrayList](#arraylist)
-   [HashMap](#hashmap)
-   [Iterators](#iterators)
-   [Conclusion](#conclusion)

## ArrayList

<div id="arraylist" />

Earlier on we discussed array objects. We created several array objects but something that we might have or not have discussed is the static size of the array object. This means that when we create an array of some size, `n`, the total number of elements this `n` sized array is `n` elements. The size of the array is not resizable.

Java provides a solution to this problem, using an `ArrayList`. With an `ArrayList` created with an initial size `n` changes as the number of elements grow.

To use an `ArrayList` we have to import it from `java.util` as `import java.util.ArrayList` and just like classes that we have used so far, we create an instance of it.

To create an instance of an `ArrayList`, we need the `type` and the initial `size`. We then create the instance like this: `ArrayList<ObjectType> arrayList = new ArrayList<ObjectType>(size);`

```java
ArrayList<Integer> numbers = new ArrayList<Integer>(5);
ArrayList<String> names = new ArrayList<>();
```

An `ArrayList` stores Objects - meaning we can't pass a primitive type to it. We can `Integer` in place of `int`, `Double` for `double`, etc. Note that in ` new ArrayList<>()`, the `type` and `size` was not passed. It would be inferred.

An `ArrayList` is a data structure (store and manage data). We can represent it logically or abstractly (ADT), just the specifications.

**ADT**:

-   Stores data of non-primitive data
-   adds an element to the list using the `add` method
-   removes an element from the list using the `remove` method
-   returns a `boolean` whether the list has a certain element using the `contains` method
-   returns the element at a specified index using the `get(index)` method
-   returns the current size of the list using the `size` method
-   removes all the elements in the list using the `clear` method

Let's create a class, `ArrayListAverage` that uses an `ArrayList` instead of an array to find the average of the elements in the array list.

<!-- convert this array code to ArrayList -->

```java
import java.util.ArrayList;

public class ArrayListAverage {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>(5);

        nums.add(3);
        nums.add(2);
        nums.add(1);
        nums.add(5);
        nums.add(4);

        int numSum = nums.get(0) + nums.get(1) + nums.get(2) + nums.get(3) + nums.get(4);

        double numAvg = (double)numSum / nums.size();

        System.out.println("Sum: " + numSum);
        System.out.println("Average: " + numAvg);

        System.out.println("\n\nadd new element and find the sum and average");

        nums.add(6);
        numSum += nums.get(5);

        numAvg = (double)numSum / nums.size();

        System.out.println("New Sum: " + numSum);
        System.out.println("New  Average: " + numAvg);
    }
}

```

Try your hands on the `contains`, `remove` and `clear` methods.

## HashMap

<div id="hashmap" />

`ArrayList` is an index based data structure just like the array and others. There is a `HashMap` which is an implementation of a `Map`. A map stores data using a key-value pair approach. This is similar to `object` in javascript and `dictionary` in python.

Just like we created an instance of the `ArrayList` class, where we passed the type of data to hold, we pass the type of the key and the value.

```java
import java.util.HashMap;

...

HashMap<String, String> hmStringKey = new HashMap<>();
HashMap<Integer, String> hmIntegerKey = new HashMap<>();
```

**ADT**

-   Stores data of non-primitive data
-   adds an element to the map using the `put(key, value)` method
-   returns a `boolean` whether the map has certain key or value using the `containsKey(key)` or `containsValue(value)` method respectively
-   return a `boolean` whether the map is equal to another map using the `equals` method
-   returns an element by key using the `get(key)` method
-   returns a `boolean` whether the map is empty using the `isEmpty` method
-   removes all the elements in the map using the `clear` method
-   removes an element from the map using the `remove` method
-   returns the current size of the map using the `size` method
-   etc

```java
import java.util.HashMap;
...

HashMap<String, String> profile = new HashMap<>();

profile.put("fullName", "John Doe");
profile.put("dob", "1st October, 1976");
profile.put("job", "Project Manager at DooDev LLC");

System.out.println(profile);
```

## Sets

<div id="sets" />

We will use the **ADT** approach to make describing Set and its operations easier.

-   Stores data of non-primitive data
-   Has no duplicate - all its elements are unique
-   adds an element to the set using the `add` method
-   returns a `boolean` whether the set has a certain element using the `contains` method
-   return a `boolean` whether the set is equal to another set using the `equals` method
-   returns a `boolean` whether the set is empty using the `isEmpty` method
-   removes all the elements in the set using the `clear` method
-   removes an element from the set using the `remove` method
-   returns the current size of the set using the `size` method

An implementation of a set is the `HashSet`. We create an instance of a `HashSet` as we did for the `ArrayList`.

There is an iterator method on `HashSet`, `ArrayList`, etc

## Iterators

<div id="iterators" />

An `Iterator` is an object that enables cycling through a collection, obtaining or removing an element. Any collection class provides an `iterator` method. An example of the `ArrayList`.

The `Iterator` ADT

-   `hasNext` method returns a `boolean` whether there is a next element
-   `next` method returns the next item
-   `remove` method removes the last next object (that is returned by the `next` method)

```java
import java.util.ArrayList;
import java.util.Iterator;

...

ArrayList<Integer> list = new ArrayList<>();
list.add(23);
list.add(34);
list.add(7);
list.add(-18);
list.add(8);
list.add(3);

// call the iterator
Iterator iterator = arrayList.iterator();

while(iterator.hasNext()) {
    System.out.println(iterator.next());
}

```

## Conclusion

<div id="conclusion" />

An array as we know has a limitation and we can bypass this limitation of our writing some hacks. Java has the `ArrayList` data structure. Its size is dynamic and can easily be used.

### Projects

-   Write a program that takes a sentence as an argument and returns a Map of the following:

    -   number of characters in the sentence with spaces
    -   number of characters in the sentence without spaces
    -   number of words in the sentence

-   Write a program that takes a sentence as an argument and returns a Map of the number of each unique character (white spaces and non-alphabetic characters like numbers and ampersand are excluded). So `hello there` will return a Map with the following keys and value pairs:

    -   h:2
    -   e:3
    -   l:2
    -   ...

### Source

-   Sololearn
-   DS Malik

<a href="#top">Top</a>
