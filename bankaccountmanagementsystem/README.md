# Bank Account Management System

## Project Description

The Bank Account Management System is a Python-based console application developed using Object-Oriented Programming (OOP). It allows users to create bank accounts, deposit and withdraw money, check balances, view transaction history, and save account records.

## Features

- Create Account
- Display Accounts
- Deposit Money
- Withdraw Money
- Check Balance
- Transaction History
- Save Account Records
- Load Account Records

## OOP Concepts Used

### Classes and Objects

Classes are used to represent bank accounts and manage banking operations.

### Encapsulation

Account details are protected using private and protected attributes and are accessed using methods.

### Inheritance

The BankAccount class inherits from the Account class.

### Abstraction

The Account class is an abstract base class that defines the display() method.

## File Handling

Account records are stored in the `accounts.csv` file.

The program supports:
- Saving account records to a CSV file.
- Loading account records from a CSV file.

## Exception Handling

The program uses `try` and `except` blocks to handle:
- Invalid user input
- File-related errors

## Project Files

- `main.py`
- `account.py`
- `bank_account.py`
- `bank_manager.py`
- `file_manager.py`
- `accounts.csv`

## How to Run

1. Open the project folder in Visual Studio Code.
2. Run:

```bash
python main.py
```

3. Select the required option from the menu.

## Conclusion

This project demonstrates the implementation of Object-Oriented Programming, File Handling, and Exception Handling by developing a simple Bank Account Management System.