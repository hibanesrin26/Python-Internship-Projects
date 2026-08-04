import csv
from bank_account import BankAccount

class FileManager:

    @staticmethod
    def save_accounts(accounts, filename="accounts.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(["Account Number", "Holder Name", "Balance"])

                for account in accounts:
                    writer.writerow([
                        account.get_account_number(),
                        account._holder_name,
                        account.get_balance()
                    ])

            print("Account data saved successfully.")

        except Exception as e:
            print("Error saving file:", e)

    @staticmethod
    def load_accounts(filename="accounts.csv"):
        accounts = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    account = BankAccount(
                        int(row[0]),
                        row[1],
                        float(row[2])
                    )
                    accounts.append(account)

        except FileNotFoundError:
            print("No existing account data found.")

        except Exception as e:
            print("Error loading file:", e)

        return accounts
    