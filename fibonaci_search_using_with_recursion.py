def fibo(num):
    if num<=1:
        return num
    else:
        return(fibo(num-1)+fibo(num-2))
limit=int(input("ENter the nth number:-"))
print(limit)
print("The sequence is:-")
for i in range(limit):
    print(fibo(i))

    
    