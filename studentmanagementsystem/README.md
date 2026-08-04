# Student Management System

## Project Description

The Student Management System is a Python-based console application developed using Object-Oriented Programming (OOP). It helps users manage student records efficiently by providing options to add, display, search, update, delete, and save student information.

## Features

* Add Student
* Display Students
* Search Student
* Update Student Marks
* Delete Student
* Save Student Records
* Load Student Records

## OOP Concepts Used

### Classes and Objects

Classes are used to represent students and manage student records. Objects are created to store individual student details.

### Encapsulation

Student data is protected inside classes and accessed through methods.

### Inheritance

The Student class inherits properties from the Person class to reuse common attributes.

### Abstraction

Abstract classes and methods are used to hide implementation details and provide a clear structure.

## File Handling

Student records are stored in the `students.csv` file.

The program supports:

* Writing student records to the CSV file
* Reading saved student records from the CSV file

## Exception Handling

The program uses `try` and `except` blocks to handle:

* Invalid user input
* Incorrect data entry
* File-related errors

## Project Files

* `main.py` - Main program file containing the menu and execution flow
* `person.py` - Contains the parent Person class
* `student.py` - Contains the Student class
* `student_manager.py` - Handles student operations such as add, search, update, and delete
* `file_manager.py` - Handles saving and loading student records
* `students.csv` - Stores student data

## How to Run

1. Open the project folder in Visual Studio Code.
2. Make sure Python is installed.
3. Run the following command:

```
python main.py
```

4. Select the required option from the menu.

## Conclusion

This project demonstrates the practical implementation of Python Object-Oriented Programming concepts, file handling, and exception handling to build a functional Student Management System.
