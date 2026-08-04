from account import Account

class BankAccount(Account):

    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(holder_name)
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = []

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawn: {amount}")
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def get_transactions(self):
        return self.__transactions

    def display(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self._holder_name}")
        print(f"Balance: {self.__balance}")