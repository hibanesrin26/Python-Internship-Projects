# Employee Payroll System

## Project Description

The Employee Payroll System is a Python-based console application developed using Object-Oriented Programming (OOP). It allows users to add employees, calculate salaries, generate payslips, search employees, and save employee records.

## Features

- Add Employee
- Display Employees
- Search Employee
- Generate Payslip
- Save Employee Records
- Load Employee Records

## OOP Concepts Used

### Classes and Objects

Classes are used to represent employees and manage payroll operations.

### Encapsulation

Employee details are protected using private and protected attributes.

### Inheritance

The Employee class inherits from the Person class.

### Abstraction

The Person class is an abstract base class that defines the display() method.

## File Handling

Employee records are stored in the `employees.csv` file.

The program supports:
- Saving employee records to a CSV file.
- Loading employee records from a CSV file.

## Exception Handling

The program uses `try` and `except` blocks to handle:
- Invalid user input
- File-related errors

## Project Files

- `main.py`
- `person.py`
- `employee.py`
- `payroll_manager.py`
- `file_manager.py`
- `employees.csv`

## How to Run

1. Open the project folder in Visual Studio Code.
2. Run:

```bash
python main.py
```

3. Select the required option from the menu.

## Conclusion

This project demonstrates the implementation of Object-Oriented Programming, File Handling, and Exception Handling by developing a simple Employee Payroll System.