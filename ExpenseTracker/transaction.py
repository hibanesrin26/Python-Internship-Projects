from abc import ABC, abstractmethod


class Transaction(ABC):

    def __init__(self, transaction_id, amount, category):
        self._transaction_id = transaction_id
        self._amount = amount
        self._category = category

    @abstractmethod
    def display(self):
        pass