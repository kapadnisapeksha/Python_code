#4.Input a number and check whether it is armstrong or not(using while)
n=int(input("Enter the number you want to check:-"))
sum=0
order=len(str(n))
copy_n=n #for loop me value of n=0 hogi tb loop end hoga to if condition check krene keliy copy_n
while(n>0):
    digit=n%10          #8891%10=1
    sum=sum+digit**order 
    n=n//10              #889%10=9,88%10=8,8%10=8
if(sum==copy_n) :  
    print(f"The Number{copy_n} is an armstrong number")  
else:
    print(f"The Number {copy_n} is not an armstrong number")   
                        