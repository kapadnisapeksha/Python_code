1. #Calculate x^y.Input x and y and calculate the answer of x to the power y(using while)

x=float(input("Enter value of x:-"))
y=float(input("Enter value of y:-"))
z=1
while(y>0):
     z=x**y
     break
print("The value of x**y is:-",z)

#without break
x=float(input("Enter value of x:-"))
y=float(input("Enter value of y:-"))
z=1
while(y>0):
     z=z*x
     y=y-1
print("The value of x**y is:-",z)
