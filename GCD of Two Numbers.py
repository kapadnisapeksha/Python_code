'''
Module: GCD of Two Numbers

The greatest common divisor (GCD) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers. After the explanation given by tuition teacher, now he wants to conduct the small test to check their understanding of GCD concept.
So, help the students by writing a program to find the GCD of Two Numbers.

Input  Format: 
The input consists of two integers.

Output  Format:
The output consists GCD of Two Numbers.

Note: All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output:
Enter the two positive numbers
12
14
GCD:2'''
# Function to compute the GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Taking input for the two numbers
print("Enter the two positive numbers")
num1 = int(input())
num2 = int(input())

# Calculate the GCD
result = gcd(num1, num2)

# Output the GCD
print(f"GCD:{result}")
   