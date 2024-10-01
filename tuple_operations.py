"""2. Define a tuple and perform the following operations on it:
i. Concatenate two tuples and display the result.
ii. Find the length of the tuple.
iii. Check if a specific element exists within the tuple.
"""
t1=(10,20,30,40,50)
t2=(60,70,80,90,100)
#i. Concatenate two tuples and display the result.
sum=t1+t2
print(f"this are two different tuples:-sum")
#ii. Find the length of the tuple.
print("lenght of tuple 1 is:-",len(t1))
print("lenght of tuple 2 is:-",len(t2))
print("lenght of concated tuple:-",len(sum))
#iii. Check if a specific element exists within the tuple.
for i in t1:
    num1=30
    if(num1==i):
        print(f"{num1} is present in tuple one")

for i in t2:
    num1=60
    if(num1==i):
        print(f"{num1}  is present in list two")