from bank_account import BankAccount

class BankManager:

    def __init__(self):
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)

    def display_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for account in self.accounts:
                account.display()
                print("-" * 20)

    def search_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def deposit_money(self, account_number, amount):
        account = self.search_account(account_number)

        if account:
            account.deposit(amount)
            print("Amount deposited successfully.")
        else:
            print("Account not found.")

    def withdraw_money(self, account_number, amount):
        account = self.search_account(account_number)

        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transaction_history(self, account_number):
        account = self.search_account(account_number)

        if account:
            print("Transaction History:")
            for transaction in account.get_transactions():
                print(transaction)
        else:
            print("Account not found.")