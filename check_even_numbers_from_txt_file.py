'''From file containing numbers separeted by comma print the count of even numbers'''
count=0
with open("numbers.txt","r")as f:
    data=f.read()
    print(data)
    num=data.split(",")
    print(num)
    for val in num:
        if(int(val)%2==0):
            count+=1
print(count)