'''Sum of the Integers in the file
Consider an input file "sample.txt" with integer values. Write a program to open the file and read the content to find the sum of all values in the file.

Rule:
The file name should be sample.txt.

Input format:
Give the input as a file which contains the integer values.

Output format:
The output will be the integer which is the sum of the integers. Display the output in the console.

Sample Input file (sample.txt):
1
2
3
4
5

Sample Output:
The sum of the integers in the file sample.txt is:15'''
#create sample.txt to run below code
#copy the path and change all e.g C:\Users\DELL\OneDrive\Desktop\sample.txt to C:/Users/DELL/OneDrive/Desktop/sample.txt
#ready to run
# main.py
with open("C:/Users/DELL/OneDrive/Desktop/sample.txt", "r") as f:
    data = f.readlines()

total_sum = 0
for val in data:
    total_sum += int(val.strip())

print(f"The sum of the integers in the file sample.txt is: {total_sum}")
