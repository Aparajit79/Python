class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isCheckedOut = False

    def checkout(self):
        if self.isCheckedOut:
            print(f"Sorry the Book {self.title}is checked Out .")
        else:
            self.isCheckedOut = True
            print(f"Successfully checked out the book {self.title}.")

    def return_book(self):
        if not self.isCheckedOut:
            print(f"Error book {self.title}is already in Library.")
        else:
            self.isCheckedOut = False
            print(f"Book {self.title}has been sucessfully returned")


book1 = book("Harry Potter", "J.K. Rowling")
book2 = book("The Hobbit", "J.R.R. Tolkien")

book1.checkout()
book1.return_book()
book2.checkout()
book2.checkout()

