
from librarian import Librarian
from book import Book
from library import Library
from member import Member

def main():
    # Initialize library and librarian
    library = Library()
    librarian = Librarian("Tasin", 20062)
    members = {}
    print("Welcome to the Library Management System!")
    while True:
        print("\nChoose an action:")
        print("1. Add a book to the library")
        print("2. Remove a book from the library")
        print("3. Display available books")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            # Add a book to the library
            book_name = input("Enter the book's title: ")
            book_author = input("Enter the book's author: ")
            book = Book(book_name, book_author)
            librarian.add_book(library, book)

        elif choice == 2:
            # Remove a book from the library
            book_name = input("Enter the title of the book to remove: ")
            librarian.remove_book(library, book_name)

        elif choice == 3:
            # Display available books
            library.display_books()

        elif choice == 4:
            # Borrow a book
            member_name = input("Enter your name: ")
            member_id = int(input("Enter your ID: "))
            #member = Member(member_name, member_id)
            if member_id in members:
                member = members[member_id]
            else:
                member = Member(member_name, member_id)
                members[member_id] = member
            book_name = input("Enter the title of the book you want to borrow: ")
            member.borrow_book(library, book_name)

        elif choice == 5:
            # Return a book
            member_name = input("Enter your name: ")
            member_id = int(input("Enter your ID: "))
           # member = Member(member_name, member_id)
            if member_id in members:
                member = members[member_id]
            else:
                member = Member(member_name, member_id)
                members[member_id] = member           
            book_name = input("Enter the title of the book you want to return: ")
            member.return_book(library, book_name)

        elif choice == 6:
            # Exit the program
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
