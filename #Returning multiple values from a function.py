#Returning multiple values from a function:
'''In other languages like C,C++ and Java, function can return atmost one value. But in 
Python, a function can return any number of values.'''
x=int(input("Enter number 1:-"))
y=int(input("Enter number 2:-"))
def multivalretn(x,y):
    sum=x+y
    sub=x-y
    rmd=x%y
    return sum,sub,rmd
result=multivalretn(x,y)
print(result)
