'''Multiple Errors Exception
In ABC Restaurant, the owner knows the total income of the restaurant per month, number of waiters and the total salary given to the waiters. He want to find the profit earned by his restaurant and the salary to be given for one waiter. 
So, write a program to find the profit and salary per waiter.

Note : 
Salary per waiter = Total Salary allocated for waiters/Number of waiters. 
Profit =  Total Income - Total Salary allocated for waiters. 
The salary per waiter and profit should be round off to two decimal places.

Input and Output Format: 
Refer sample input and output for formatting specifications. 
All text in bold corresponds to input and the rest corresponds to output. 

This program may generate:
1. Zero Division Error Exception when the number of waiters is 0. 
2. Name Error exception. 
3. ValueError Exception may occur with a non-numeric input.
Use exception handling mechanisms to handle these exceptions. 

Sample Input and Output 1: 
Enter the Income of the Restaurant per month 
100000 
Enter the No of Waiters 
3 
Enter the salary allocated for the waiters 
1000 
Profit: 99000.00 
Salary per Waiter: 333.00 

Sample Input and Output 2: 
Enter the Income of the Restaurant per month 
q 
Exception has been occured'''

def calculate_profit_and_salary():
    try:
        income = float(input("Enter the Income of the Restaurant per month\n"))
        num_waiters = int(input("Enter the No of Waiters\n"))
        total_salary = float(input("Enter the salary allocated for the waiters\n"))

        salary_per_waiter = total_salary // num_waiters
        profit = income - total_salary

        print(f"Profit: {profit:.2f}")
        print(f"Salary per Waiter: {salary_per_waiter:.2f}")

    except (ValueError, ZeroDivisionError, NameError) as e:
        print("Exception has been occured")

calculate_profit_and_salary()   