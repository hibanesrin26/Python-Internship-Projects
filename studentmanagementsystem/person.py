from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod
    def display(self):
        pass