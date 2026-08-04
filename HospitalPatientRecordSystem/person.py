from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, person_id, name, age):
        self._person_id = person_id
        self._name = name
        self._age = age

    @abstractmethod
    def display(self):
        pass