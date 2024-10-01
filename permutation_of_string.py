def generate_permitution(input_str):
    n=len(input_str)
    all_permitation=[]

    def permite(current_index):
        if current_index==n-1:
            all_permitation.append(''.join(input_str))
            return
        for i in range(current_index,n):
          input_str[current_index],input_str[i]= input_str[i],input_str[current_index]
          permite(current_index+1)
          input_str[current_index],input_str[i]= input_str[i],input_str[current_index]
    permite(0)
    return all_permitation

input_string=input("enter the string")
userstring=list(input_string)
permutitions=generate_permitution(userstring)
print("All permutations of '{}' are:".format(''.join(input_string)))

for i in  permutitions:
     print(i)




     