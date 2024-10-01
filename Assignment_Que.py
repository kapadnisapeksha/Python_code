#1. Take marks of 6 subjects in a list and calculate their percentage. 
#if percentage>75 print distinction if percentage>60 print first class, 
#if percentage>45 print second class else display fail
a=[]
sum=0
p=int(input("Enter the six element:-"))
for i in range(0,p):
    x=int(input("Enter the marks of 6 subject:-"))
    a.append(x)
print(a)
for i in a:
    sum=sum+i
    percentage=sum/6
print(f"your percentage is {percentage}")

if(percentage>75):
    print(f"congratulation,you are passed with distinction {percentage} percentage ")
elif(percentage>60):
    print(f"congratualation you are passed with first class with {percentage} percentage")
elif(percentage>45):
    print(f"congratulation you are passed with second class with {percentage} percentage")
else:
    print("better luck next time'you are fail'")




