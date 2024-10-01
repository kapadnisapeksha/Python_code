'''Date Format Validate

Harry a class 11th  student who was good at programming. Harry wanted to validate the date into a standard format, but we were lazy to enter the date into the standard to avoid his practice. So Harry planned to write a program that validate's the given date.

Image result for validate

So try to develop a python program which validates the standard date format (dd/MM/yyyy)

Problem Constraints:
Use Regex Expression Module
Use the Match method to vacillate the date format.

Input format:
The single line of input in date format(dd/MM/yyyy)

Output format:
Single Line string value "Valid" if it matches standard date format
else specify it as "Invalid" in which it is wrong(date, month or year)

Refer sample input and output)

Sample Input 1:
05/04/2012
Sample output 1:
Valid

Sample Input 2:
1/1/2000
Sample output 2:
Invalid date
Invalid month'''
import re

text = input()

# Correct patterns to match the date format
pattern = r'\d{2}/\d{2}/\d{4}'
# pattern1 = r'(\d{2})/(\d{2})/(\d{4})'

match = re.match(pattern, text)
# print(match)

if match is not None:
    print("Valid")
else:
    parts = text.split('/')
    if len(parts) == 3:
        date, month, year = parts[0], parts[1], parts[2]
        if re.match(r'^\d{2}$', date) is None:
            print("Invalid date")
        if re.match(r'^\d{2}$', month) is None:
            print("Invalid month")
        if re.match(r'^\d{4}$', year) is None:
            print("Invalid year")
    # else:
    #     print("Invalid date format")