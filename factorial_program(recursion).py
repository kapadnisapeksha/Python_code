def factorial(n):
    if n==0:
        result=1
    else :
        result=n*factorial(n-1)
        return result
    
print("Factorial of 4 is :",factorial(4))