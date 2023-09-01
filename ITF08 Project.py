import re

class Book:
    id_counter = 0

    def __init__(self, title, author, level):
        Book.id_counter += 1
        self.book_id = Book.id_counter
        self.title = title
        self.author = author
        self.level = level.upper()
        self.is_available = True

class Member:
    id_counter = 0

    def __init__(self, name, email, level):
        Member.id_counter += 1
        self.member_id = Member.id_counter
        self.name = name
        self.email = email
        self.level = level.upper()
        self.borrowed_books = []

    def borrow_book(self, book):
        if self.level == book.level and book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print("This book is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name} has returned '{book.title}'.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def add_member(self, member):
        self.members.append(member)
        print("Member added successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Level: {book.level}, Availability: {'Available' if book.is_available else 'Not Available'}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            for member in self.members:
                print(f"ID: {member.member_id}, Name: {member.name}, Email: {member.email}, Level: {member.level}")

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def edit_member(self, member_id, new_name, new_email, new_level):
        member = self.find_member_by_id(member_id)
        if member:
            member.name = new_name
            member.email = new_email
            member.level = new_level.upper()
            print("Member information updated successfully.")
        else:
            print("Member not found.")

    def delete_member(self, member_id):
        member = self.find_member_by_id(member_id)
        if member:
            self.members.remove(member)
            print("Member deleted successfully.")
        else:
            print("Member not found.")


def validate_member_name_input(name):
    if len(name) < 3:
        print("Please enter a name with at least three letters.")
        return False
    return True


def validate_book_name_input(title):
    if len(title) < 3 or not re.match("^[a-zA-Z0-9]+$", title):
        print("Please enter a book title with at least three letters or numbers.")
        return False
    return True


def validate_author_input(author):
    if len(author) < 1 or not any(char.isalnum() for char in author):
        print("Please enter at least one letter or number for the author.")
        return False
    return True


def validate_member_email_input(email):
    if len(email) < 3 or not re.match("^[a-zA-Z0-9!@#$%^&*()_+{}\[\]:;<>,.?~_-]+$", email):
        print("Please enter a valid email with at least three characters.")
        return False
    return True


def validate_level_input(level):
    return level.upper() in {'A', 'B', 'C'}


library = Library()
print(' Welcome to the Library System '.center(100, '-'))
while True:
    print("\nLibrary Management System Menu:")
    print("1. Add Member")
    print("2. Edit Member")
    print("3. Show Members")
    print("4. Delete Member")
    print("5. Add Book")
    print("6. Show Books")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter member's name: ")

        if not validate_member_name_input(name):
            print("Invalid entry. Please start over.")
            continue

        email_attempts = 3
        while email_attempts > 0:
            email = input("Enter member's email: ")
            if validate_member_email_input(email):
                break
            else:
                print("Please enter a valid email with at least three characters.")
                email_attempts -= 1
        if email_attempts == 0:
            print("Invalid choice. Please start over.")
            continue

        level_attempts = 3
        while level_attempts > 0:
            level = input("Enter member's level (A/B/C): ").upper()
            if not validate_level_input(level):
                print("Please enter your level from within the choices available.")
                level_attempts -= 1
            else:
                break
        if level_attempts == 0:
            print("Invalid choice. Please start over.")
            continue

        new_member = Member(name, email, level)
        library.add_member(new_member)

    elif choice == '2':
        member_id = int(input("Enter member ID to edit: "))
        new_name = input("Enter new name: ")

        if not validate_member_name_input(new_name):
            print("Invalid entry. Please start over.")
            continue

        new_email_attempts = 3
        while new_email_attempts > 0:
            new_email = input("Enter new email: ")
            if validate_member_email_input(new_email):
                break
            else:
                print("Please enter a valid email with at least three characters.")
                new_email_attempts -= 1
        if new_email_attempts == 0:
            print("Invalid choice. Please start over.")
            continue

        level_attempts = 3
        while level_attempts > 0:
            new_level = input("Enter new level (A/B/C): ").upper()
            if not validate_level_input(new_level):
                print("Please enter your level from within the choices available.")
                level_attempts -= 1
            else:
                break
        if level_attempts == 0:
            print("Invalid choice. Please start over.")
            continue

        library.edit_member(member_id, new_name, new_email, new_level)

    elif choice == '3':
        library.display_members()

    elif choice == '4':
        member_id = int(input("Enter member ID to delete: "))
        library.delete_member(member_id)

    elif choice == '5':
        title = input("Enter book title: ")

        if not validate_book_name_input(title):
            print("Invalid entry. Please start over.")
            continue

        author_attempts = 3
        while author_attempts > 0:
            author = input("Enter book author: ")
            if validate_author_input(author):
                break
            else:
                print("Please enter at least one letter or number for the author.")
                author_attempts -= 1
        if author_attempts == 0:
            author = "Unknown"

        level_attempts = 3
        while level_attempts > 0:
            level = input("Enter book level (A/B/C): ").upper()
            if not validate_level_input(level):
                print("Please enter your level from within the choices available.")
                level_attempts -= 1
            else:
                break
        if level_attempts == 0:
            print("Invalid choice. Please start over.")
            continue  

        new_book = Book(title, author, level)
        library.add_book(new_book)
        library.display_books()

    elif choice == '6':
        library.display_books()

    elif choice == '7':
        member_id = int(input("Enter member ID: "))
        book_title = input("Enter book title: ")
        member = library.find_member_by_id(member_id)
        book = library.find_book_by_title(book_title)
        if member and book:
            member.borrow_book(book)
        else:
            print("Member or book not found.")

    elif choice == '8':
        member_id = int(input("Enter member ID: "))
        book_title = input("Enter book title: ")
        member = library.find_member_by_id(member_id)
        book = library.find_book_by_title(book_title)
        if member and book:
            member.return_book(book)
        else:
            print("Member or book not found.")

    elif choice == '9':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
