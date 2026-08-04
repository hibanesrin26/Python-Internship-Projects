from student import Student
from course import Course
from registration_manager import RegistrationManager
from file_manager import FileManager


manager = RegistrationManager()

manager.registrations = FileManager.load_registrations()


while True:

    print("\n===== Course Registration System =====")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Register Course")
    print("4. Drop Course")
    print("5. Display Registrations")
    print("6. Save Data")
    print("7. Exit")


    choice = input("Enter your choice: ")


    try:


        if choice == "1":

            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")

            student = Student(
                student_id,
                name
            )

            manager.add_student(student)

            print("Student added successfully.")



        elif choice == "2":

            course_id = int(input("Enter Course ID: "))
            course_name = input("Enter Course Name: ")

            course = Course(
                course_id,
                course_name
            )

            manager.add_course(course)

            print("Course added successfully.")



        elif choice == "3":

            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))

            manager.register_course(
                student_id,
                course_id
            )



        elif choice == "4":

            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))

            manager.drop_course(
                student_id,
                course_id
            )



        elif choice == "5":

            manager.display_registrations()



        elif choice == "6":

            FileManager.save_registrations(
                manager.registrations
            )



        elif choice == "7":

            FileManager.save_registrations(
                manager.registrations
            )

            print("Thank you for using Course Registration System.")

            break



        else:

            print("Invalid choice.")


    except ValueError:

        print("Please enter valid input.")


    except Exception as e:

        print("Error:", e)