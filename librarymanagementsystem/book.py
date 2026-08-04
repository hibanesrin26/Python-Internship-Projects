from library_item import LibraryItem

class Book(LibraryItem):

    def __init__(self, book_id, title, author, available=True):
        super().__init__(title, author)
        self.__book_id = book_id
        self.__available = available

    def get_book_id(self):
        return self.__book_id

    def get_available(self):
        return self.__available

    def set_available(self, status):
        self.__available = status

    def display(self):
        print(f"Book ID: {self.__book_id}")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Available: {'Yes' if self.__available else 'No'}")