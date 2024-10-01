#WAP to perfore even index elemnt of list

a=[2,4,5,7,6,8,9,1,6.16,16.7,9,45.2]
itrate_list=0
for i in a:
    itrate_list+=1 #puri list traverse hogi len milti hai
for n in range(0,itrate_list,2):
    print(a[n])
   