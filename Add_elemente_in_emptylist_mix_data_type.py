a=[]
intnum=int(input("Enter how many int element you want to add:-"))
floatnum1=int(input("Enter how many int element you want to add:-"))
strin=int(input("Enter how many int element you want to add:-"))
for i in range(0,intnum+1):
    x=int(input("ENter the integer element in the list:-"))
    a.append(x)
for i in range(0,floatnum1+1):
    y=float(input("Enter the float valur elemnt in the list:-"))
    a.append(y)
for i in range(0,strin+1):
    z=str(input("Enter the string value element in the list:-"))
    a.append(z)
print(a)