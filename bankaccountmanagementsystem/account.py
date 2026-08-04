from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, holder_name):
        self._holder_name = holder_name

    @abstractmethod
    def display(self):
        pass