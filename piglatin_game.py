a=input("Enter the word:-")
b=['a','e','o','u','i']
if(a[0]=='a' or a[0]=='e'or a[0]=='o' or a[0]=='u' or a[0]=='i'):
    print(a[1::]+a[0]+'ay')
else:
    print(a+"way")  