from transaction import Transaction


class Expense(Transaction):

    def __init__(self, transaction_id, amount, category, date):
        super().__init__(
            transaction_id,
            amount,
            category
        )

        self.__date = date


    def get_id(self):
        return self._transaction_id


    def get_amount(self):
        return self._amount


    def get_category(self):
        return self._category


    def get_date(self):
        return self.__date


    def display(self):

        print(f"Transaction ID: {self._transaction_id}")
        print(f"Amount: {self._amount}")
        print(f"Category: {self._category}")
        print(f"Date: {self.__date}")