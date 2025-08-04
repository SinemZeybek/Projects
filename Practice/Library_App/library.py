import datetime 

class Person:
    def __init__(self, full_name):
        self.full_name = full_name

class Book:
    def __init__(self, title, author, book_id, genre, can_be_rented):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True
        self.genre = genre
        self.can_be_rented = can_be_rented


    def __str__(self):
        status = "Available" if self.available else "Not available"
        rental_status = "can be rented" if self.can_be_rented else " "
        return f"{self.title} by {self.author} | ID: {self.book_id}, {status}, {rental_status} Genre: {self.genre}"


class Member(Person):  
    def __init__(self, member_id, full_name):
        super().__init__(full_name)
        self.member_id = member_id
        self.borrowed_books = []
        self.active = True
        self.balance = 0.0

    def __str__(self):
        active_status = "Active" if self.active else "Deactive"
        return f"Name: {self.full_name}, ID: {self.member_id} ({active_status}), Balance: ${self.balance}"
    

class Staff(Person):    #burada superle getirdik.
    def __init__(self, full_name, job):
        super().__init__(full_name)
        self.job = job

    def __str__(self):
        return f"Staff: {self.full_name} / Job: {self.job}"
    
class Library:
    rental_fee = 5.0
    book = None
    member = None

    def __init__(self):
        self.books = []
        self.members = []
        self.staff = []
        self.book_loans = []
        self.member_counter = 103     # çünkü 101, 102 önceden ekliyoruz

#####################################################
    def add_balance(self, member_id, amount):
        for m in self.members:
            if m.member_id == member_id:
                m.balance += amount
                print(f"{amount}$ added. New balance: {m.balance}$")
                return
        print("Member not found.")

        
    def validate(self, member_id, book_id, is_extra_controls=True):
        self.member = None
        self.book = None

        for m in self.members:
            if m.member_id == member_id:
                self.member = m
                break

        for b in self.books:
            if b.book_id == book_id:
                self.book = b
                break
       
        if not self.member or not self.book:
            print("Member or book not found.")
            return False
        
        if not self.member.active:
            return False
        
            print
               
        if is_extra_controls: 
            if self.book in self.member.borrowed_books:
                print("This member already has this book.")
                return False
            if len(self.member.borrowed_books) >= 3:
                print("A member can borrow max. 3 books.")
                return False
            if not self.book.available:
                print("This book is not available at the moment.")
                return False
            
        return True
    

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def add_staff(self, staff):
        self.staff.append(staff)

    def show_books(self):
        for book in self.books:
            if book.available == True:
                print(book)

    def show_rentable_books(self):
        print("Rentable Books: ")
        for book in self.books:
            if book.can_be_rented and book.available:
                print(book)

    def search_by_genre(self, genre):
        self.genre = genre
        print(f"{genre} Books: ")
        found = False
        for book in self.books:
            if book.genre.lower().strip() == genre.lower().strip():
                print(book)
                found = True
        if not found:
            print("No books found in this genre.")

    def show_members(self):
        print("Active Members: ")
        for member in self.members:
            if member.active:
                print(member)

    def show_staff(self):
        print("Staff List: ")
        for s in self.staff:
            print(s)

    def register_member(self, full_name):
        new_member = Member(self.member_counter, full_name)
        self.member_counter += 1
        self.add_member(new_member)
        print(f"Registration successful! Member ID: {new_member.member_id}")
#########################################
    def loan_book(self, member_id, book_id):
        if not self.validate(member_id, book_id):
            return

        if self.book.can_be_rented:
            if self.member.balance < Library.rental_fee:
                print("Insufficient balance. Please add money to your balance to rent this book.")
                return
            self.member.balance -= Library.rental_fee
            print(f"{Library.rental_fee}$ rental fee deducted. Remaining balance: {self.member.balance}$")
        
        self.book.available = False
        self.member.borrowed_books.append(self.book)
        print(f"{self.book.title} was borrowed by {self.member.full_name}.")


    
    def return_book(self, member_id, book_id):
        if not self.validate(member_id, book_id, is_extra_controls=False):
            return         
        self.member.borrowed_books.remove(self.book)
        self.book.available = True
        print(f"{self.book.title} has been returned by {self.member.full_name}.")


    def list_member_books(self, member_id):
            for m in self.members:
                if m.member_id == member_id:
                    self.member = m
                    break

            if not self.member:
                print("Member not found.")
                return

            if not self.member.borrowed_books:
                print(f"{self.member.full_name} has no borrowed books at the moment.")
                return

            print(f"Books borrowed by {self.member.full_name}:")
            for book in self.member.borrowed_books:
                print(f"- {book.title}")

    def show_members(self):
        print("Active Members: ")
        for m in self.members:
            if m.active:
                print(f"{m.full_name}, ID: {m.member_id}")

    def change_member_status(self, member_id):
        for m in self.members:
            if m.member.id == member_id:
                m.active = not m.active
                status = "activated" if m.active else "deactivated"
                print(f"{m.full_name} with {m.member_id} ID number, has been {status}")
                return
            print("Member not found.")





# Program Start: 
library = Library()

# Adding books
library.add_book(Book("1984", "George Orwell", 1, "Dystopian", True))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 2, "Classic", False))
library.add_book(Book("Les Misérables", "Victor Hugo", 3, "Historical Fiction", True))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 4, "Classic", True))
library.add_book(Book("Animal Farm", "George Orwell", 5, "Satire", False))


# Adding members
library.add_member(Member(101, "Alice Johnson"))
library.add_member(Member(102, "Bob Smith"))

# Adding staff
library.add_staff(Staff("Emma Wilson", "Librarian"))

# Menu 
while True:
    print("\n Library System")
    print("1. List all books")
    print("2. Register as a new member")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View member's borrowed books")
    print("6. List active members")
    print("7. Deactivate/Activate a member")
    print("8. Add balance to a member")
    print("9. Search books by genre")
    print("10. Exit")

    
    choice = input("Your choice: ")

    if choice == "1":
        library.show_books()
    elif choice == "2":
        name = input("Enter your name: ")
        library.register_member(name)
    elif choice == "3":
        try:
            member_id = int(input("Enter your member ID: "))
            book_id = int(input("Enter the book ID to borrow: "))
            library.loan_book(member_id, book_id)
        except ValueError:
            print("Please enter valid numbers.")
    elif choice == "4":
        try:
            member_id = int(input("Enter your member ID: "))
            book_id = int(input("Enter the book ID to return: "))
            library.return_book(member_id, book_id)
        except ValueError:
            print("Please enter valid numbers.")
    elif choice == "5":
        try:
            member_id = int(input("Enter member ID: "))
            library.list_member_books(member_id)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "6":
        library.show_members()
    elif choice == "7":
        try:
            member_id = int(input("Enter member ID to toggle status: "))
            library.change_member_status(member_id)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "8":
        try:
            member_id = int(input("Enter member ID: "))
            amount = float(input("Enter amount to add: "))
            library.add_balance(member_id, amount)
        except ValueError:
            print("Please enter valid numbers.")
    elif choice == "9":
        genre = input("Enter genre to search: ")
        library.search_by_genre(genre)

    elif choice == "10":
        print("Bye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 8.")
