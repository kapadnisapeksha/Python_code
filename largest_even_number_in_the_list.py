#WAP to print larget even number in the list ,take a list from user
a=[]
largest_even_num=0
intnum=int(input("Enter how many int element you want to add:-"))
for i in range(0,intnum+1):
    x=int(input("ENter the integer element in the list:-"))
    a.append(x)

print(a)
for j in a:
    if(j%2==0):
        if(j>largest_even_num):
            largest_even_num=j
print(largest_even_num)
    




    