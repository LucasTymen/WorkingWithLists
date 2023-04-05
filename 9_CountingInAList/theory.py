"""
Working with Lists in Python
Counting in a List

In Python, it is common to want to count occurrences of an item in a list.

Suppose we have a list called letters that represents the letters in the word “Mississippi”:
"""
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
"""
If we want to know how many times i appears in this word, we can use the list method called .count():
"""
num_i = letters.count("i")
print(num_i)
"""
Would output:

4

Notice that since .count() returns a value, we can assign it to a variable to use it.

We can even use .count() to count element appearances in a two-dimensional list.

Let’s use the list number_collection as an example:
"""
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
"""
If we wanted to know how often the sublist [100, 200] appears:
"""
num_pairs = number_collection.count([100, 200])
print(num_pairs)
"""
Would output:

2

Let’s count some list items using the .count() method!
Instructions
1.

Mrs. Wilson’s class is voting for class president. She has saved each student’s vote into the list votes.

Use .count() to determine how many students voted for "Jake" and save the value to a variable called jake_votes.

If we wanted to know how many students voted for "Laurie", we’d use:

votes.count("Laurie")

2.

Use print() to examine jake_votes.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    If the item being counted isn’t in the list, will count() return an error?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
