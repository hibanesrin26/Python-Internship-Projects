import csv
from expense import Expense


class FileManager:


    @staticmethod
    def save_expenses(expenses, filename="expenses.csv"):

        try:

            with open(filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Transaction ID",
                    "Amount",
                    "Category",
                    "Date"
                ])


                for expense in expenses:

                    writer.writerow([
                        expense.get_id(),
                        expense.get_amount(),
                        expense.get_category(),
                        expense.get_date()
                    ])


            print("Expense data saved successfully.")


        except Exception as e:

            print("Error saving file:", e)



    @staticmethod
    def load_expenses(filename="expenses.csv"):

        expenses = []


        try:

            with open(filename, "r") as file:

                reader = csv.reader(file)

                next(reader)


                for row in reader:

                    expense = Expense(
                        int(row[0]),
                        float(row[1]),
                        row[2],
                        row[3]
                    )

                    expenses.append(expense)


        except FileNotFoundError:

            print("No expense data found.")


        except Exception as e:

            print("Error loading file:", e)


        return expenses