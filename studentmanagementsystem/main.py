from student import Student
from student_manager import StudentManager
from file_manager import FileManager

manager = StudentManager()

# Load existing students
manager.students = FileManager.load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Save Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))

            student = Student(student_id, name, age, marks)
            manager.add_student(student)

            print("Student added successfully.")

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            student = manager.search_student(student_id)

            if student:
                student.display()
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = int(input("Enter Student ID: "))
            marks = float(input("Enter New Marks: "))
            manager.update_marks(student_id, marks)

        elif choice == "5":
            student_id = int(input("Enter Student ID: "))
            manager.delete_student(student_id)

        elif choice == "6":
            FileManager.save_students(manager.students)

        elif choice == "7":
            FileManager.save_students(manager.students)
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)