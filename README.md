## SDSS Computing Studies Python Assignment
### Assignment #005 Tuples and Lists (Total Marks 12)

Objectives:
* Understand the difference between a tuple and a list
* Convert between tuples and lists
* Find the length of a list or tuple
* Access specific elements in a list or tuple
* Add or insert an element into a list
* Remove elements from a list
* Sort a list
* Use math operators to join 2 lists
* Create new lists


Last class we introduced the concept of a tuple.  A tuple is a collection of data
that contains multiple elements.  For example, it might contain information about
the latitude and longitude of a location on a map:
'''
location = (123.10012, -1.33321)
'''

or a tuple might contain information about your student record:
'''
me = ("Joe Luncbox","876561")
'''

A tuple is an unordered collection of data, but can not be changed.  The data in a 
tuple cannot be edited or deleted.

A *list* is similar to a tuple, but the data CAN be changed.
See the file example1.py to see how tuples and lists differ.

A list is more flexible, because you can add or remove items from the list. 
The commands for adding to a list are done a bit differently from most of the
commands that we have looked at thus far. 
example2.py will go through some of the commands involved in modifying a list

There are other imporant methods available when working with lists.
example3.py will show you how we can sort() lists, count() the number of times
that something appears, and find the index() of something that we are looking
for inside a list.

### XX Tasks

##### Task 1
Create a list that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

(2 points) 

##### Task 2
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list

(2 points)

##### Task 3
Sort the given list by numerical value
Find the smallest and the largest value and display them.
1 mark will come from an assertion test (variables will be checked) and 1 mark will come from an input/output test

(2 marks)

##### Problem 1
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.
(2 marks)

##### Problem 2
Print the list named "fruit".
Ask the user to enter a word
If the word is in the list, delete all occurrences of that word from the list
If the word is not in the list, add the word to the list
Print out the updated list
(2 marks)

##### Problem 3
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added
(2 marks)
