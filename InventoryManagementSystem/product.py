from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_id, name, price):
        self._product_id = product_id
        self._name = name
        self._price = price

    @abstractmethod
    def display(self):
        pass