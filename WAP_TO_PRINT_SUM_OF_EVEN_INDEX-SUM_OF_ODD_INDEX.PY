#WAP to print sum of even index number -sum of odd index numbers
a=[]
sum_of_even=0
sum_of_odd=0

num=int(input("enter the total number of elemnts in list:-"))
for i in range(0,num+1):
    x=int(input("enter the values of the elements:-"))
    a.append(x)
    l1=len(a)
for j in range(0,l1):
    if(j%2==0):
      sum_of_even=sum_of_even+a[j]
    elif(j%2!=0):
     sum_of_odd+=a[j]
print(f"sum of even numbers is:-{sum_of_even}")

print(f"sum of odd mnumber is:-{sum_of_odd}")

total=sum_of_even-sum_of_odd
print(f"TOtal sum of is:-{total}")
