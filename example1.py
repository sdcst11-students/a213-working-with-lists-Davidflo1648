#!python3

'''
tuples are sets of data that are unordered, 
can have data that repeats, and can not be changed:
note that they are defined with round brackets
the tuple can contain mixed variable types
individual elements in a tuple can be accessed using
the index of the element, starting at 0 for the first element

To see some of the different ways you can access elements of a list or tuple,
open up example1b.py
'''

print("====== Tuple Examples =====")
myTuple = (10,20,1,10,5)
myOtherTuple = ("Joe","Fred",3,"12")

print( myTuple[1] )
print( myOtherTuple[2] )

# Lists are almost identical to tuples, except they are defined
# using [] and the data inside them can be changed.
print("\n\n")
print("====== List Examples =====")
myList = [10,20,1,10,5]
myOtherList = ["Joe","Fred",3,"12"]

print( myList[1] )
print( myOtherList[2] )

print("\n\n")
print("==== demonstration of tuple/list element assignment ===")
# to demonstrate how they can be changed, uncomment
# the lines below

# Uncommeent the 2 lines below to see an error if we try to
# change an element in a tuple and print it
#myTuple[1] = "tuple!"
#print( myTuple[1])

# Uncommeent the 2 lines below to see an error if we try to
# change an element in a list and print it
#myList[1] = "list!"
#print( myList[1] )

# Whether you have a list or a tuple, you can still count how many elements
# they have using the len() command:

print("\n\n")
print("=== Counting elements in lists and tuples ===")
tupleLength = len(myTuple)
print( "myTuple contains " + str(tupleLength) + " elements")

listLength = len(myList)
print( "myList contains " + str(listLength) + " elements")
