"""3. Cumulative sum means, if the list is [a,b,c....] then its cumulative sum is[a,a+b,a+b+c....]. 
Write a program to input a list and store the cumulative sum of the list in another list and display it"""
a=[]
x=int(input("enter the total number in list:-"))
for i in range(0,x+1):
    p=int(input("Enter the values of element:-"))
    a.append(p)
print(a)
cummutive_sum_list=[]
cummutive_sum=0
for n in a:
    cummutive_sum +=n
    cummutive_sum_list.append(cummutive_sum)
print(cummutive_sum_list)

 

