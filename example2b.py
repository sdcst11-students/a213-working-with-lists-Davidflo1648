#! python3
"""
Commands to remove elements from lists:

list.remove( element )   - removes the first occurrence of an element from the list
list.pop() - removes the element at a specific index

"""
print("\n\n=== Examples for how list.remove() works ===")
print("going to remove 'apple' twice.  Which one is removed each time?")
myList = ["apple","banana","orange","cherry","apple","kiwi"]
print(myList)
myList.remove("apple")
print(myList)
myList.remove("apple")
print(myList)
print("\n\n")

print("=== Examples for how list.pop() works ===")
print("going to use .pop(3) to remove an element. Which element is removed?")
myList = ["apple","banana","orange","cherry","apple","kiwi"]
print(myList)
myList.pop(3)
print(myList)
