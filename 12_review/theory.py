"""
Working with Lists in Python
Review

In this lesson, we learned how to:

    Add elements to a list by index using the .insert() method.
    Remove elements from a list by index using the .pop() method.
    Generate a list using the range() function.
    Get the length of a list using the len() function.
    Select portions of a list using slicing syntax.
    Count the number of times that an element appears in a list using the .count() method.
    Sort a list of items using either the .sort() method or sorted() function.

As you go through the exercises, feel free to use print() to see changes when not explicitly asked to do so.
Instructions
1.

Our friend Jiho has been so successful in both the flower and grocery business that she has decided to open a furniture store.

Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.

First, how many items are in the warehouse?

Save the answer to a variable called inventory_len.

Use len to find the number of items in inventory
2.

Select the first element in inventory. Save it to a variable called first.

If we wanted to select the second element in inventory, we would use:

second = inventory[1]

Remember that Python lists are zero-indexed.
3.

Select the last element from inventory. Save it to a variable called last.

The last item has index -1.
4.

Select items from the inventory starting at index 2 and up to, but not including, index 6.

Save your answer to a variable called inventory_2_6.

If we wanted to select items from the inventory starting at index 5 and up to, but not including, index 7, we would use:

inventory_5_7 = inventory[5:7]

5.

Select the first 3 items of inventory. Save it to a variable called first_3.

If we wanted to select the first 5 items from inventory, we would use:

inventory[:5]

6.

How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.

If we wanted to know how many 'dresser's were in inventory, we would use:

num_dressers = inventory.count('dresser')

7.

Remove the 5th element in the inventory. Save the value to a variable called removed_item.

Since lists in Python of zero_indexed, the 5th element will be at index 4.

Use the .pop() method to remove elements from a list by index.
8.

There was a new item added to our inventory called "19th Century Bed Frame".

Use the .insert() method to place the new item as the 11th element in our inventory.

Since lists in Python of zero_indexed, the 11th element will be at index 10.
9.

Sort inventory using the .sort() method or the sorted() function.

Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().

Print inventory to see the result.

As a reminder here is how you might use .sort() or sorted()

# Using sort
list.sort()

# Using sorted
list = sorted(list)

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Is it possible to sort() a list but do it in reverse order?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
