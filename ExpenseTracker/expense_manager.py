class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)


    def display_expenses(self):

        if not self.expenses:
            print("No expenses found.")

        else:
            for expense in self.expenses:
                expense.display()
                print("-" * 20)


    def search_expense(self, transaction_id):

        for expense in self.expenses:

            if expense.get_id() == transaction_id:
                return expense

        return None


    def delete_expense(self, transaction_id):

        expense = self.search_expense(transaction_id)

        if expense:
            self.expenses.remove(expense)
            print("Expense deleted successfully.")

        else:
            print("Expense not found.")


    def monthly_summary(self):

        total = 0

        for expense in self.expenses:
            total += expense.get_amount()

        print("Total Monthly Expense:", total)