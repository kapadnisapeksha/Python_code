import library_catlog_system as l
print("Press 1 to add new book")
print("Press 2 to search new book")
print("Press 3 to display the  book")
print("Press 4 to check out the book")
print("Press 5 to exist")
n=int(input("Enter the choice:-"))
while True :
    if(n==1):
        l.add_book()
    elif(n==2):
        l.search_book()
    elif(n==3):
        l.dispaly()
    elif(n==4):
        l.checkout_book()
    elif(n==5):
        l.exit()
        break
    else:
        print("Enter the valid choice")

