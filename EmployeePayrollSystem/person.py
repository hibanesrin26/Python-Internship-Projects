from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def display(self):
        pass