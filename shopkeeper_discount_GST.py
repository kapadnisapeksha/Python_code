# the shopkeeper give 10% discount on printed price.6% GST is added into printed price. 
#calculate and display total amount paid by the customer

printed_price=float(input("Enter the printed price on product:-"))
discount=printed_price*0.1
GST=printed_price*0.06
total_amount_to_pay=printed_price-discount+GST
print("TOtal amount paid by customer is:-",total_amount_to_pay)