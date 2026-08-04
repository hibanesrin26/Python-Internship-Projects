import csv
from book import Book

class FileManager:

    @staticmethod
    def save_books(books, filename="books.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(["Book ID", "Title", "Author", "Available"])

                for book in books:
                    writer.writerow([
                        book.get_book_id(),
                        book._title,
                        book._author,
                        book.get_available()
                    ])

            print("Book data saved successfully.")

        except Exception as e:
            print("Error saving file:", e)

    @staticmethod
    def load_books(filename="books.csv"):
        books = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    book = Book(
                        int(row[0]),
                        row[1],
                        row[2],
                        row[3] == "True"
                    )
                    books.append(book)

        except FileNotFoundError:
            print("No existing book data found.")

        except Exception as e:
            print("Error loading file:", e)

        return books