#How to read multiple values from the keyboard in a single line:
a,b=[int(x) for x in input("Enter two number:-").split()]
print("Product of two numbers:-",a*b)