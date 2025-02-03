class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display(self):
        print(f"Book details are : \n Title : {self.title} \n Author : {self.author} \n ISBN : {self.isbn}")
        
        
b = Book("Islands", "Tagore", 123456)
b.display()
        
        
#Dynamic

'''title = input("Enter the title \n")
author = input("enter the author \n")
isbn = input("enter isbn \n")

b = Book(title,author,isbn)
b.display()'''