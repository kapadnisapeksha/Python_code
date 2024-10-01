"""4. Write a program to find median of the list
PS-Median, in statistics, is the middle value of the given list of data when arranged in an order

"""
a=[]
sum=0
x=int(input("total number of elements in list:-"))
for i in range(0,x):
    p=int(input("Enter the values of elements:-"))
    a.append(p)
a.sort()
no_of_elements=(len(a))
print(a)
for j in a:
    sum+=j

    avg=sum/no_of_elements
    median_position=a[0]+a[-1]/2

print(f"Average of the list is:-{avg}")
print(f"Median of the list is:-{median_position}")
