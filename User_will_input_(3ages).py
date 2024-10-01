'''1. User will input (3ages).Find the oldest one'''
a=int(input("enter the 3 ages:-"))
b=int(input("enter the 3 ages:-"))
c=int(input("enter the 3 ages:-"))
if(a>b and a>c):
    print(f"{a}is older")

elif(a<b and c<b):
    print(f"{b} is older")

else:
    print(f"{c} is older ")


