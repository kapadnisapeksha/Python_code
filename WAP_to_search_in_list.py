#WAP to8,9,1 serach given number is in list or not
a=[1,2,3,4,5,6,7,8,9,10]
ser=int(input("Enter the number you want search in list:-"))
for i in a:
    if i==ser:
        print(a.index(i))



  