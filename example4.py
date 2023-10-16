#!python3

# some different ways to find the largest number in a list:

#method 1
#sort the list, find the last entry
values = [3,4,5,1,2,1,6]
values.sort()
print(values[-1])

#method 2
#sort the list, 
#count how many entries, 
#find the entry at the last position but remember:
# we start counting at 0, so the last position for 8 entries
# is position 7 so we subtract 1 from the number of entries
values = [3,4,5,1,2,1,6]
length = len(values)
print(values[length-1])


