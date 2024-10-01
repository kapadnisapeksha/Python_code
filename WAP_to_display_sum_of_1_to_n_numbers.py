#sum of 1 to n numbers take input from user for n
n=int(input("Enter the nth number:-"))
i=1
s=0
while(i<=n):
    s=i+s
    i=i+1
print("sum of the numbers is:-",s)