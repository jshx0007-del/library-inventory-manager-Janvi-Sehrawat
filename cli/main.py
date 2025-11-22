import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from library_manager.inventory import LibraryInventory
from library_manager.book import Book


def show_menu():
    print("\n====== Library Inventory Manager ======\n")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")


def main():
    library = LibraryInventory()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")

            try:
                library.add_book(Book(title, author, isbn))
                print("Book added successfully!")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            isbn = input("ISBN to issue: ")
            try:
                library.issue_book(isbn)
                print("Book issued!")
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            isbn = input("ISBN to return: ")
            try:
                library.return_book(isbn)
                print("Book returned!")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            books = library.display_all()
            if not books:
                print("No books available.")
            else:
                print("\n--- Books ---")
                for book in books:
                    print(book)

        elif choice == "5":
            sub = input("Search by (1) Title or (2) ISBN? ")
            if sub == "1":
                title = input("Enter the title: ")
                results = library.search_by_title(title)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("No books found.")
            elif sub == "2":
                isbn = input("Enter ISBN: ")
                book = library.search_by_isbn(isbn)
                if book:
                    print(book)
                else:
                    print("Book not found.")
            else:
                print("Invalid search option.")

        elif choice == "6":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
