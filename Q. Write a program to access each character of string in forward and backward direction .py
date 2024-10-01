'''Q. Write a program to access each character of string in forward and backward direction 
by using while loop? '''

line = "python is easy to learn"
t = len(line)

# Forward direction using for loop
print("Forward direction:")
for i in range(t):
    print(line[i],end=' ')

# Backward direction using for loop
print("\nBackward direction:")
for i in range(t - 1, -1, -1):
    print(line[i])
