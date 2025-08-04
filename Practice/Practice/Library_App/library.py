import datetime 

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.available = True  # True means book is available


    def __str__(self):
        return f"{self.title} by {self.author}: (Book ID: {self.book_id}, {'Available' if self.available else 'Not available'})"


class Member:
    def __init__(self, member_id, full_name):
        self.member_id = member_id
        self.full_name = full_name
        self.email = self.generate_email(full_name)
        self.borrowed_books = []

    def generate_email(self, full_name):
        name = full_name
        replacements = {
            ' ': '.'
        }
        for old, new in replacements.items():
            name = name.replace(old, new)
        return f"{name}@email.com"

    def __str__(self):
        return f"Name: {self.full_name}, E-mail: {self.email}, Member Number: {self.member_id}, Loaned Books: {self.borrowed_books} "
    

class Staff:
    def __init__(self, full_name, job):
        self.full_name = full_name
        self.job = job

    def __str__(self):
        return f"Staff: {self.full_name} / {self.job}"
    
class Library: 
    def __init__(self):
        self.books = []
        self.members = []
        self.staff = []
        self.book_loans = []
        self.member_counter = 103     # çünkü 101, 102 önceden ekliyoruz

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def add_staff(self, staff):
        self.staff.append(staff)

    def show_books(self):
        for book in self.books:
            print(book)

    def register_member(self, full_name):
        new_member = Member(self.member_counter, full_name)
        self.member_counter += 1
        self.add_member(new_member)
        print(f"Registration successful! Member ID: {new_member.member_id}")

    def loan_book(self, member_id, book_id):
        # Üye ve kitap bul
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        book = None
        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        # Kontroller
        if not member or not book:
            print("Üye veya kitap bulunamadı.")
            return

        if book in member.borrowed_books:
            print("Bu kitap zaten bu üyeye verilmiş.")
            return

        if not book.available:
            print("Bu kitap şu anda müsait değil.")
            return

        if len(member.borrowed_books) >= 3:
            print("Bir üye en fazla 3 kitap alabilir.")
            return

        # Kitabı ödünç ver
        book.available = False
        member.borrowed_books.append(book)
        print(f"{book.title} adlı kitap {member.full_name} adlı üyeye verildi.")

    def return_book(self, member_id, book_id):
            member = None
            for m in self.members:
                if m.member_id == member_id:
                    member = m
                    break

            book = None
            for b in self.books:
                if b.book_id == book_id:
                    book = b
                    break

            if not member or not book:
                print("Member or book not found.")
                return

            if book not in member.borrowed_books:
                print("This book is not borrowed by this member.")
                return

            member.borrowed_books.remove(book)
            book.available = True
            print(f"{book.title} has been returned by {member.full_name}.")



    def list_member_books(self, member_id):
            member = None
            for m in self.members:
                if m.member_id == member_id:
                    member = m
                    break

            if not member:
                print("Member not found.")
                return

            if not member.borrowed_books:
                print(f"{member.full_name} has not borrowed any books yet.")
                return

            print(f"Books borrowed by {member.full_name}:")
            for book in member.borrowed_books:
                print(f"- {book.title}")



# ------------ Program Start ------------
library = Library()

# Add books
library.add_book(Book("1984", "George Orwell", 1))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 2))
library.add_book(Book("Les Misérables", "Victor Hugo", 3))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 4))
library.add_book(Book("Animal Farm", "George Orwell", 5))

# Add members
library.add_member(Member(101, "Alice Johnson"))
library.add_member(Member(102, "Bob Smith"))

# Add staff
library.add_staff(Staff("Emma Wilson", "Librarian"))

# ------------ Menu Loop ------------
while True:
    print("\n Library System")
    print("1. List all books")
    print("2. Register as a new member")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. View member's borrowed books")
    print("6. Exit")
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 6.")