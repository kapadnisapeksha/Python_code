# To add  all elements to list upto 100 which are divisible by 10 
list=[]
for i in range(101):
    if i%10==0:
        list.append(i)
print(list)