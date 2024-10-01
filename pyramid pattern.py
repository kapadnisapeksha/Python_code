# pyramid pattern
n=7
for i in range(n):
    for j in range(i,n-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

#reverse pyramid
print("reverse pyramid")
n=7
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(2* i-1):
        print("*",end="")
    print()