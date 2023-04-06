"""
Working with Lists in Python
Sorting Lists II

A second way of sorting a list in Python is to use the built-in function sorted().

The sorted() function is different from the .sort() method in two ways:

    It comes before a list, instead of after as all built-in functions do.
    It generates a new list rather than modifying the one that already exists.

Let’s return to our list of names:

names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]

Using sorted(), we can create a new list, called sorted_names:

sorted_names = sorted(names)
print(sorted_names)

This yields the list sorted alphabetically:

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

Note that using sorted did not change names:

print(names)

Would output:

['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

Instructions
1.

Use sorted() to order games and create a new list called games_sorted.

As with any built-in function, pass the list you wish to be sorted in between the parenthesis ( ) of the function.

sorted(list)

2.

Print both games and games_sorted. How are they different?

In contrast to the method .sort(), the built-in function sorted() will not modify the original list.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Both sort() and sorted() can be used to sort a list. What is the difference between them and when would I want to use one versus the other?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
