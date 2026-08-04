from bank_account import BankAccount
from bank_manager import BankManager
from file_manager import FileManager

manager = BankManager()

# Load existing accounts
manager.accounts = FileManager.load_accounts()

while True:
    print("\n===== Bank Account Management System =====")
    print("1. Create Account")
    print("2. Display Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Transaction History")
    print("7. Save Accounts")
    print("8. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            account_number = int(input("Enter Account Number: "))
            holder_name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))

            account = BankAccount(account_number, holder_name, balance)
            manager.create_account(account)

            print("Account created successfully.")

        elif choice == "2":
            manager.display_accounts()

        elif choice == "3":
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Deposit Amount: "))
            manager.deposit_money(account_number, amount)

        elif choice == "4":
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Withdraw Amount: "))
            manager.withdraw_money(account_number, amount)

        elif choice == "5":
            account_number = int(input("Enter Account Number: "))
            account = manager.search_account(account_number)

            if account:
                print("Current Balance:", account.get_balance())
            else:
                print("Account not found.")

        elif choice == "6":
            account_number = int(input("Enter Account Number: "))
            manager.transaction_history(account_number)

        elif choice == "7":
            FileManager.save_accounts(manager.accounts)

        elif choice == "8":
            FileManager.save_accounts(manager.accounts)
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)