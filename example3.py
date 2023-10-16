#!python3

"""
There are many times when you need to search for data within a list
myList.index(element)  will find the index that a specific element is located in the list
myList.count(element)  will count the number of times that a specific element appears in the list
myList.sort()          will sort a list by numerical or alphabetical order.  It updates the current list
"""
print("\n\n=== Miscellaneous tuple/list commands")
myList = ["Delta", "Echo", "Foxtrot","Alpha", "Golf", "Baker", "Charlie"]
print(myList)
print("Sorting the list using the command myList.sort()")
myList.sort()
print(myList)
print("\n")
dIndex = myList.index("Delta")
dCount = myList.count("Delta")
print("Delta is found at index " + str(dIndex) + " using myList.index('Delta') ")
print("The number of times Delta appears can be found with myList.count('Delta') :" + str(dCount))
