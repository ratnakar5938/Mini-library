"""
Create a library class
"""

class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lend_detail = {}

    def get_details(self):
        print(f"{self.library_name} is the name of this library\n")
        self.show_books()
        print("")
        self.lend_details_books()
        print("")

    def show_books(self):
        print("The following books are available in the library: ")
        for item in self.list_of_books:
            print(item)

    def lend_details_books(self):
        print("The following is the books lent to the users: ")
        for book3, user3 in self.lend_detail.items():
            print(f"'{book3}' has been issued by {user3}")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        print("Your book has been added to the library")
        self.show_books()

    def lend_book(self, book_name, user_name):
        lend = False
        for item in self.list_of_books:
            if item == book_name:
                self.list_of_books.remove(book_name)
                print("Book has been issued")
                self.lend_detail[book_name] = user_name
                lend = True
                break
            else:
                for book1, user1 in self.lend_detail.items():
                    if book1 == book_name:
                        print(f"{book1} has been issued by {user1}")
                        lend = True
                        break
                break
        if lend:
            pass
        else:
            print("Book is neither present in the library nor lent to any user")

    def return_book(self, book_name, user_name):
        for book2, user2 in self.lend_detail.items():
            if book2 == book_name and user2 == user_name:
                del self.lend_detail[book2]
                self.list_of_books.append(book2)
                print("Book has been returned")
                break
            else:
                print("Book has not been issued or u entered something else")

if __name__ == '__main__':
    RaviLibrary = Library(["Alice and the wonderland", "Harry potter", "Sherlock Holmes", "Head first java", "Hands on machine learning"], "Ravi Library")
    while True:
        user = input("Enter your name: ")
        print(f"Hii {user}!!! Welcome to {RaviLibrary.library_name}")
        option = input("Enter a to add book, l to lend book, r to return book, g to get details about the library, s to see the books, ld for see lent books: ")
        if option == 'a':
            book = input("Enter book name: ")
            RaviLibrary.add_book(book)
        elif option == 'l':
            book = input("Enter book name: ")
            RaviLibrary.lend_book(book, user)
        elif option == 'r':
            book = input("Enter book name: ")
            RaviLibrary.lend_book(book, user)
        elif option == 'g':
            RaviLibrary.get_details()
        elif option == 's':
            RaviLibrary.show_books()
        elif option == 'ld':
            RaviLibrary.lend_details_books()
        else:
            print("You entered something else!!!")
        end = input("Press q to end if there is nothing more u want to do else just press enter: ")
        if end == "q":
            exit()
        else:
            pass