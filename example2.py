#! python3
"""
lists can be modified, unlike tuples, but the commands to do so can be a bit different.
The basic commands are:

list.append()
list.insert()
list.remove( element )   - removes the first occurrence of an element from the list
list.pop() - removes the element at a specific index

Note that to use these commands, you include the variable name when calling the command.
These commands that are used with "dot" notation (a dot between the object and the command) are
sometimes called "methods"

example2b.py will show you how the .remove() and .pop() methods work
"""
print("=== Examples for how list.append() works ===")
myList = ["apple","banana","orange","cherry","apple","kiwi"]
print("going to myList.append('strawberry'). Where is it added?\n")
print(myList)

myList.append("strawberry")
print(myList)
print("\n\n")

print("=== Examples for how list.insert() works ===")
myList = ["apple","banana","orange","cherry","apple","kiwi"]
print("going to myList.insert(3, 'strawberry'). Where is it added?\n")
print(myList)
myList.insert(3, "strawberry")
print(myList)
print("\n\n")

print("=== Creating a list")
# note that you can create a list using variables or numbers or strings!
a = 10
newList = (a , "hello", 14)
print(newList)

