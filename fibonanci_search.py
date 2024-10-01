n=int(input("Enter the limit:-"))
n1=0
n2=1
for i in range(1,n+1,1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
