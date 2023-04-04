"""
##################################   Python List Methods    #################################################
# .count()              a list method to count the number off occurences of an element in a list            #
# .insert()             a list method to insert an element into a specific index of a list                  #
# .pop()                a list method to remove an element from a spacific index or from the end of a list  #
# range()               a built-in method Python function to create a sequence of integers                  #
# len()                 a built-in method Python function to get the lengh of a list                        #
# .sort() / sorted()    a method and a built-in function to sort a list                                     #
#############################################################################################################


Working with Lists in Python
Working with Lists

Now that we know how to create and access list data, we can start to explore additional ways of working with lists.

In this lesson, you’ll learn how to:

    Add and remove items from a list using a specific index.
    Create lists with continuous values.
    Get the length of a list.
    Select portions of a list (called slicing).
    Count the number of times that an element appears in a list.
    Sort a list of items.

Note: In some of the exercises, we will be using built-in functions in Python. If you haven’t yet explored the concept
of a function, it may look a bit new. Below we compare it to the method syntax we learned in the earlier lesson.

Here is a preview:

# Example syntax for methods
list.method(input)

# Example syntax for a built-in function
builtinfuncion(input)

Instructions

Take a second to preview some of the things we will be learning by examining the graphic of common list methods and
built-in functions.

When you’re ready, continue to the next exercise.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Is it possible to sort() a list but do it in reverse order?

Still have questions? View this exercise's thread in the Codecademy Forums.

##########################################################################################################
https://www.codecademy.com/resources/docs/python/built-in-functions?page_req=catalog
Built-in Functions

The Python interpreter has a set of functions and types built into it (pre-defined). They are always ready at your
disposal; you can use them without needing to import a library.

There are 68 built-in functions and they are listed here in alphabetical order.
Built-in Functions

abs()
    Returns the absolute value of a numeric argument.
all()
    Returns True if every item in an iterable evaluates to True, otherwise, it returns False.
any()
    Takes in an iterable object such as a list or tuple and returns True if any of the elements in the iterable are
    True. If none of the elements in the iterable are True, returns False.
ascii()
    Receives as input an object containing string data, and returns the object as a printable representation with
    escapes for non-ASCII characters (accented characters).
bin()
    Converts an integer into its binary equivalent string.
bool()
    Converts a value to a Boolean True or False value.
breakpoint()
    Engages, configures, and changes the debugger program used in a script.
bytearray()
    Returns an array of the given bytes of an object.
bytes()
    Returns a byte immutable object representing the given bytes of an object.
callable()
    Returns True if an object is callable, and False if an object is not callable.
chr()
    Returns Unicode characters represented by integers ranging between 0 and 1,114,111.
classmethod()
    Converts a given function into a class method.
compile()
    Returns a runnable code object created from a string.
complex()
    Converts a given string into a complex number.
delattr()
    Allows the user to delete attributes from an object.
dict()
    Initializes a new dictionary from mapping n-number of object (key, value) pairs.
eval()
    Returns the value of a Python expression passed as a string.
filter()
    Returns a filter object that applies a function to each item in an iterable and returns the values that are True.
float()
    Returns a float value based on a string, numeric data type, or no value at all.
frozenset()
    Returns a new frozenset using an optional iterable object such as a string or list.
hasattr()
    Returns True if an object has an attribute and False otherwise.
help()
    Displays documentation of an object using the Python help utility.
input()
    Prompts the user for data and returns it as a string.
int()
    Takes in a value that can be converted into an integer, and returns a copy of the value in the int datatype.
isinstance()
    Returns True if the given object is the specified type. Otherwise the function will return False.
issubclass()
    Returns True if a given class is a subclass of one or more classes.
len()
    Returns the length of an object, which can either be a sequence or collection.
list()
    Returns a list from an iterable.
map()
    Returns an iterator that takes a function and applies it to every item in an iterable.
max()
    Returns the highest value from values given or an iterable.
min()
    Returns the lowest value from values given or an iterable.
next()
    Returns the next element from an iterable object.
open()
    Used for opening files in a Python program.
pow()
    Returns the value of a base number x to the power of an exponent y, with an optional modulus z.
print()
    Prints the string representation of an object.
range()
    Returns a sequence of numbers based on the given range
reversed()
    Takes in an iterator object, such as a list or string, and returns a reversed iterator object.
round()
    Takes a number and an integer as parameters, and returns the number with decimal places equal to the integer.
set()
    Returns a new set based on an optional iterable object such as a list.
sorted()
    Takes in an iterator object, such as a list, tuple, dictionary, set, or string, and sorts it according to a parameter.
str()
    Takes in a value that can be converted into a string, and returns a copy of the value in the string datatype.
super()
    Returns a temporary object that allows a given class to inherit the methods and properties of a parent or sibling class.
tuple()
    Creates a new tuple.
type()
    Returns the data type of the argument passed to the function.
zip()
    Takes multiple iterators as input and returns a single zip object made up of a list of tuples.
"""
