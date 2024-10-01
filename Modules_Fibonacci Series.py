'''Module: Fibonacci Series
The teacher was teaching about number series generation and one of the series is like she will write first two number of the series and each student has to write a next number of the series on the board and next number will be the addition of previous two numbers and first two numbers will be 0 and 1. 
So, help the students by writing a program to generate the Fibonacci series.

Input Format:  
The input consists of integer which represents 'n' as number of values in the series

Output Format:
The output consists of series of integer numbers.

Sample Input 1:
3
Sample Output1:
0 1 1

Sample Input 2:
6
Sample Output2:
0 1 1 2 3 5'''
# Function to generate the Fibonacci series up to n numbers
def generate_fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    series = [0, 1]
    for i in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
    
    return series

# Taking input for the number of values in the series
n = int(input() )

# Generate the Fibonacci series
fibonacci_series = generate_fibonacci_series(n)

# Output the Fibonacci series
print(' '.join(map(str, fibonacci_series)))
   