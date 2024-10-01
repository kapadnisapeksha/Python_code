#4. Library charges fine if the book is returned late as given below

#	1 - 5 ===== 40 paisa per day
	
#	6 - 10 ===== 60 paisa per day

#	above 10 days ===== 80 paisa per day

#	input number of days the book is late and then calculate the fine and 	display it

lated_days=int (input("Enter the number of days you late to submit:-"))
if(lated_days>=1 and lated_days<=5):
    fine=lated_days*40
    print("Pay the fine:-",fine)
elif(lated_days>=6 and lated_days<=10):
    fine=lated_days*60
    print("Pay the fine:-",fine)
elif(lated_days<=10):
    fine=lated_days*80
    print("Pay the fine:-",fine)
else:
    exit()

