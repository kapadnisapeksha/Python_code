n=int(input("ENter the count of numbers:-"))

for _ in range (n):
    mob_num=input().strip()
    
    if (len(mob_num)==10 and mob_num.isdigit()):
        if (mob_num[0] in '789'):
            print("YES")
        else:
            print("NO")
    else:
        print('No')