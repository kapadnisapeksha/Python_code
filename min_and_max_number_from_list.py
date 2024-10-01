#WaP to print min and max number in the list
a=[]
x=int(input("Enter total number you want in list:-"))
#min_num=a[0]

for i in range(0,x+1):
    p=float(input("Enter the number:-"))
    a.append(p)
for i in a:
    max_num=a[0]
    if(i>max_num):
        max_num=i
print(f"max number is:-{max_num}")
for j in a:
    min_num=a[0]
    if(j<min_num):
        min_num=j
print(f"min_number in list is {min_num}")