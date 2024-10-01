n=[10,20,[30,40],[50,60],[70,80]]
print(n)
print(n[2])
print(n[2][0])
print(n[2][1])
#nested list as matrix in python
print ("List row wise:-")
for i in n:
    print (i)
#printing the list in matrix form
  
for i in range(len(n)):   
    for j in range(len(n[i])):   
        print(n[i][j],end=' ')   
    print()  