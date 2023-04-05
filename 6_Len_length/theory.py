"""
Working with Lists in Python
Length

Often, we’ll need to find the number of items in a list, usually called its length.

We can do this using a built-in function called len().

When we apply len() to a list, we get the number of elements in that list:
"""
my_list = [1, 2, 3, 4, 5]

print(len(my_list))
"""
Would output:

5

Let’s find the length of various lists!
Instructions
1.

Calculate the length of long_list and save it to the variable long_list_len.

To use the len() built-in function, pass a list in between the parenthesis ( )
"""
example_list = [1, 5, "Item"]
list_length = len(example_list)
"""
2.

Use print() to examine long_list_len.

Your output should be 18.
3.

We have provided a completed range() function for the variable big_range.

Calculate its length using the function len() and save it to a variable called big_range_length.

Note: Range objects do not need to be converted to lists in order to determine their length

We can use the len() function to calculate a range’s length.
"""
# Generates a range of (0, 5)
my_range = range(0, 10, 5)

length_of_range = len(my_range)
"""
4.

Use print() to examine big_range_length.

Your output should be 300
5.

Change the range() function that generates big_range so that it skips 100 instead of 10 steps between items.

How does this change big_range_length?

Changing the third input of a range changes how many elements we skip and thus changing the length of the list. For example:
"""
# The list would be [0, 2, 4, 6, 8] with length 5
range(0, 10, 2)

# The list would be [0, 3, 6, 9] with length 4
range(0, 10, 3)
"""
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    What is the relationship between the value returned by len() and the indexes which can be used to access elements of a list?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
