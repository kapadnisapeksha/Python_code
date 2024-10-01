# Q. Write a program to dispaly *'s in Right angled triangled form
# Using 1 for loop 
for i in range(5):
    print("*"*i)
    i +=1 # (i +=1 === i=i+1)

# 2.using two for loop
print("Pattern using 2 for loop")
for i in range (1,5):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
        # i+=1


