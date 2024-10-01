book=[]
def add_book():
    title=input("Enter the title of the book:-")
    author=input("Enter the author of the book:-")
    genre=input("ENter the genre of the book:-")
    book.append(add_book)

def search_book():
    search=input("Enter the book title:-")
    for i in book:
        if(search==i):
            print("Book Found in our library")
        else:
            print("Book not found")

def dispaly():
    print(book)

def checkout_book():
    check=input("Enter the title of the book:-")
    for i in book:
        if(check==i):
            book.remove(check)
        else:
            print("Book not found")
def exit():
    print("Thank you !!! visit again")

