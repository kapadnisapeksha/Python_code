try:
    n=int(input("Enter the number:-"))
    m=int(input("Enter the number:-"))
    z=n/m
    print(z)
except ValueError:
    print("Enter integer value only")
except ZeroDivisionError:
    print("number can not divide by zero")
