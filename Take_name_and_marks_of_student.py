'''Q. Write a program to enter name and percentage marks in a dictionary and 
display information on the screen
'''
dic={}
n=int(input("Enter the number of student:-"))

for i in range(n):
    name=input("Enter the name of student:-")
    marks=int(input("Enter the % marks of student:-"))
    dic[name]=marks
print("Name of Student","\t","% of marks") 
for x in dic:
    print("\t",x,"\t\t",dic[x])

