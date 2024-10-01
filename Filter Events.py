'''Filter Events 
 

Write a program to get size of list and its elements and  to find numbers divisible by thirteen from a list using anonymous function (Lambda) and display those numbers.

Input Format:
The first line of input corresponds to the size of list 'n'.
The next 'n' line of input corresponds to the elements in the list .

Output Format:
The output consists of numbers divisible by thirteen separated by space.
Refer sample output for formatting specifications.
 

Problem Constraints:
n > 0 print the numbers divisible by thirteen separated by space, else display as "Invalid input".

Sample Input/Output 1:
Enter size of list
9
Enter the elements in list
12
65
54
39
102
339
221
50
70
65 39 221

Sample Input/Output 2:
Enter size of list
O
Invalid input
 '''
# Get the size of the list
size_element = int(input("Enter size of list\n"))

# Check for invalid input
if size_element <= 0:
    print("Invalid input")
else:
    # Initialize an empty list
    elements = []

    # Get each element of the list
    print("Enter the elements in list")
    for i in range(size_element):
        add_l_ele = int(input())
        elements.append(add_l_ele)

    # Find numbers divisible by thirteen using a lambda function
    divisible_by_thirteen = list(filter(lambda x: x % 13 == 0, elements))

    # Print the result
    if divisible_by_thirteen:
        print(" ".join(map(str, divisible_by_thirteen)))
    else:
        print("No numbers divisible by thirteen found")