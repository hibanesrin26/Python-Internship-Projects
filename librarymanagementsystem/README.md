# Library Management System

## Project Description

The Library Management System is a Python-based console application developed using Object-Oriented Programming (OOP). It helps users manage library books by allowing them to add, display, search, issue, return, and save book records.

## Features

- Add Book
- Display Available Books
- Search Book
- Issue Book
- Return Book
- Save Book Records
- Load Book Records

## OOP Concepts Used

### Classes and Objects

Classes are used to represent books and manage library operations. Objects are created to store individual book details.

### Encapsulation

Book data is protected using private and protected attributes and accessed through getter and setter methods.

### Inheritance

The Book class inherits properties from the LibraryItem class.

### Abstraction

The LibraryItem class is an abstract class that defines the display() method, which is implemented in the Book class.

## File Handling

Book records are stored in the `books.csv` file.

The program supports:
- Saving book records to a CSV file.
- Loading book records from a CSV file.

## Exception Handling

The program uses `try` and `except` blocks to handle:
- Invalid user input
- File-related errors

## Project Files

- `main.py` - Main program containing the menu and program execution.
- `library_item.py` - Abstract base class.
- `book.py` - Book class.
- `library_manager.py` - Handles library operations.
- `file_manager.py` - Handles file operations.
- `books.csv` - Stores book records.

## How to Run

1. Open the project folder in Visual Studio Code.
2. Make sure Python is installed.
3. Run:

```bash
python main.py
```

4. Select the required option from the menu.

## Conclusion

This project demonstrates the implementation of Object-Oriented Programming concepts, file handling, and exception handling by developing a simple Library Management System.