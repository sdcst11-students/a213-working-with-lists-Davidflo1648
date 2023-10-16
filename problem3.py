#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""
integers = []
for i in range(10):
    userinput = input("Enter an integer:")
    try:
        num = int(userinput)
        if num == -1:
            break
        elif num > 0:
            integers.append(num)
        else:
            print("Invalid input. Please enter a positive integer or -1 to stop.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

max_int = max(integers)

print(f"The largest number you entered is {max_int}")
