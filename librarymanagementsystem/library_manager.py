from book import Book

class LibraryManager:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                if book.get_available():
                    book.display()
                    print("-" * 20)

    def search_book(self, book_id):
        for book in self.books:
            if book.get_book_id() == book_id:
                return book
        return None

    def issue_book(self, book_id):
        book = self.search_book(book_id)

        if book:
            if book.get_available():
                book.set_available(False)
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        book = self.search_book(book_id)

        if book:
            if not book.get_available():
                book.set_available(True)
                print("Book returned successfully.")
            else:
                print("Book is already available.")
        else:
            print("Book not found.")