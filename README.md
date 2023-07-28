### Tuple_in_python

Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a Python list in terms of indexing, nested objects, 
and repetition but the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.

#### Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#### Ordered

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

#### Unchangeable

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#### Allow Duplicates

Since tuples are indexed, they can have items with the same value:

### Advantages of Tuple over List in Python

Since tuples are quite similar to lists, both of them are used in similar situations.

However, there are certain advantages of implementing a tuple over a list:

We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.

Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.

Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.

If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
