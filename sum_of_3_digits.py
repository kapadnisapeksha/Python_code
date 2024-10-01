'''4. Write a program that will give you the sum of 3 digits
'''

def add(a,b,c):
    
    sum1=a+b+c
    return sum1
    
a=float(input("Enter Num1:-"))
b=float(input("Enter Num2:-"))
c=float(input("Enter Num3:-"))

obj=add(a,b,c)


print(f"sum of 3 Num is {obj}")
