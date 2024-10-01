'''Q.  Write a program to take a tuple of numbers from the keyboard and print its sum and 
average? '''

t=eval(input("Enter Tuple of Numbers:"))   
l=len(t)   
sum=0   
for x in t:   
     sum=sum+x   
print("The Sum=",sum)   
print("The Average=",sum/l)   

'''tuple=eval(input("Enter the tuple numbrs:-"))
l=len(tuple)
sum=0
for i in tuple:
    sum=sum+i
print(sum)'''