'''Sum of Elements
 

Write a program to get size of list and  elements of the list and to find the sum of all the numbers inside the list, with the help of Lambda Expression and display the sum of elements.

Input Format:
The first line of input corresponds to the size of list 'n'.
The next 'n' line of input corresponds to the elements in the list .

Refer sample input for formatting specifications.

Output Format:
The output consists of sum of elements in the list.

Refer sample output for formatting specifications.
 

Problem Constraints:
n > 0 print the sum of the elements in the list, else display as "Invalid Input".
 

Sample Input/Output 1:

Enter the number of elements in list
6
Enter the elements
5
8
10
20
50
100
The sum of of elements in list is 193

Sample Input/Output 2:

Enter the number of elements in list
0
Invalid Input'''
size = int(input("Enter the number of elements in list\n"))
if size <= 0:
    print("Invalid Input")
else:
    elements = []
    print("Enter the elements")
    for i in range(size):
        in_element = int(input())
        elements.append(in_element)
    
    # Calculate the sum using a lambda expression
    sum_of_elements = (lambda x: sum(x))(elements)
    
    print(f"The sum of  of elements in list is {sum_of_elements}")