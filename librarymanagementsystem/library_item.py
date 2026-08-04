from abc import ABC, abstractmethod

class LibraryItem(ABC):

    def __init__(self, title, author):
        self._title = title
        self._author = author

    @abstractmethod
    def display(self):
        pass