#5. Bank of india gives interest on the rates given below as per number of years. Calculate and display the simple intereast based on general citizen and senior citizen(general citizen means age if less than 60 and senior citizen means age is greater than 60)

#Nubmber of years       citizen			ROI
#1 -2				    senior			7.5
#				        general			6.5
	
#2-4				    senior			8.5
#				        general			7.5

#4-6				    senior			9.5
#				        general			8.5

#above 6 years		    senior			10
#				        general			9.5

no_of_years=int(input("Enter Number of yers:-"))
amount=int(input("Enter the amount:-"))
age=int(input("enter your age:-") )
#time=no_of_years*12
if(no_of_years<=2 and no_of_years>=1):
    
        if(age>= 60):
                simple_interest=(amount*7.5)/100
                total_amount=simple_interest+amount
                print("Simple interest is:-",simple_interest)
                print("Total amount (senior citizien) is:-",amount)
        
        else:
               simple_interest=(amount*no_of_years*6.5)/100
               print("Simple interest is:-",simple_interest)
               print("Total amount (senior citizien) is:-",amount)

elif(no_of_years>=2 and no_of_years<=4):
        
        if(age>=60 ):
                simple_interest=(amount*no_of_years*8.5)/100
                print("Simple interest is:-",simple_interest)
                print("Total amount (senior citizien) is:-",amount)
        
        else:
               simple_interest=(amount*no_of_years*7.5)/100
               print("Simple interest is:-",simple_interest)
               print("Total amount (senior citizien) is:-",amount)
elif(no_of_years>4 and no_of_years<=6):   
        if(age>=60 ):
                simple_interest=(amount*no_of_years*9.5)/100
                print("Simple interest is:-",simple_interest)
                print("Total amount (senior citizien) is:-",amount)        
        else:
               simple_interest=(amount*no_of_years*8.5)/100
               print("Simple interest is:-",simple_interest)
               print("Total amount (senior citizien) is:-",amount)
elif(no_of_years>6):
        if(age>=60 ):
                simple_interest=(amount*no_of_years*10)/100
                print("Simple interest is:-",simple_interest)
                print("Total amount (senior citizien) is:-",amount)
        
        else:
               simple_interest=(amount*no_of_years*9.5)/100
               print("Simple interest is:-",simple_interest)
               print("Total amount (senior citizien) is:-",amount)
        

                
                
                
    



