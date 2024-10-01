def palidrome(a):
    a=121
    rev=0
    rem=0
    t=a
    while(a!=0):
        rev=a%10
        rem=(rev*10)+rem
        n=a//10
    if(t==rem):
        print(f"{t} is palindrome")
    else:
        print(f"{t} is not palindrome")

palidrome(1221)