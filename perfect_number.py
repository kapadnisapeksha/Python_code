#WAP to check the number is perfect number or not
n=int(input("Enter the number:-"))
i=1
sum=0
while(i<n):
    if(n%i==0):
       sum=sum+i
    i+=1
if(sum==n):
    print(f"{n} is perfect number")
else:
     print(f"{n} is not a perfect number")
    