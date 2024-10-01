n=int(input("Enter the number:-"))
rem=1
rev=0
while(n!=0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print(f"Reverse number is:-{rev}")
