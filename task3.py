#! python3
"""
Sort the given list by numerical value
Find the smallest and the largest value and display them:

inputs:
none

outputs:
string containing the 2 numbers:

example:
The smallest number is 3 and the largest number is 9
"""

myList = [ 3,6,5,4,6,7,8,6,5,9,4,5 ]
myList.sort()

smallest = myList[0]
largest = myList[-1]

output = f"The smallest number is {smallest} and the largest number is {largest}"
print(output)
