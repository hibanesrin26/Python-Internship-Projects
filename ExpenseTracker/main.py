from expense import Expense
from expense_manager import ExpenseManager
from file_manager import FileManager


manager = ExpenseManager()

# Load existing expenses
manager.expenses = FileManager.load_expenses()


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Monthly Summary")
    print("6. Save Expenses")
    print("7. Exit")


    choice = input("Enter your choice: ")


    try:

        if choice == "1":

            transaction_id = int(input("Enter Transaction ID: "))
            amount = float(input("Enter Amount: "))
            category = input("Enter Category: ")
            date = input("Enter Date: ")


            expense = Expense(
                transaction_id,
                amount,
                category,
                date
            )

            manager.add_expense(expense)

            print("Expense added successfully.")



        elif choice == "2":

            manager.display_expenses()



        elif choice == "3":

            transaction_id = int(
                input("Enter Transaction ID to search: ")
            )


            expense = manager.search_expense(transaction_id)


            if expense:
                expense.display()

            else:
                print("Expense not found.")



        elif choice == "4":

            transaction_id = int(
                input("Enter Transaction ID: ")
            )

            manager.delete_expense(transaction_id)



        elif choice == "5":

            manager.monthly_summary()



        elif choice == "6":

            FileManager.save_expenses(
                manager.expenses
            )



        elif choice == "7":

            FileManager.save_expenses(
                manager.expenses
            )

            print("Thank you for using Expense Tracker.")

            break



        else:

            print("Invalid choice.")


    except ValueError:

        print("Please enter valid input.")


    except Exception as e:

        print("Error:", e)