from book import Book
from library_manager import LibraryManager
from file_manager import FileManager

manager = LibraryManager()

# Load existing books
manager.books = FileManager.load_books()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Available Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Save Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            manager.add_book(book)

            print("Book added successfully.")

        elif choice == "2":
            manager.display_books()

        elif choice == "3":
            book_id = int(input("Enter Book ID: "))
            book = manager.search_book(book_id)

            if book:
                book.display()
            else:
                print("Book not found.")

        elif choice == "4":
            book_id = int(input("Enter Book ID: "))
            manager.issue_book(book_id)

        elif choice == "5":
            book_id = int(input("Enter Book ID: "))
            manager.return_book(book_id)

        elif choice == "6":
            FileManager.save_books(manager.books)

        elif choice == "7":
            FileManager.save_books(manager.books)
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)