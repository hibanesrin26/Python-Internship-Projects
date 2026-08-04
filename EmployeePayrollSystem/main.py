from employee import Employee
from payroll_manager import PayrollManager
from file_manager import FileManager

manager = PayrollManager()

# Load existing employees
manager.employees = FileManager.load_employees()

while True:
    print("\n===== Employee Payroll System =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Generate Payslip")
    print("5. Save Employees")
    print("6. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            basic_salary = float(input("Enter Basic Salary: "))

            employee = Employee(employee_id, name, basic_salary)
            manager.add_employee(employee)

            print("Employee added successfully.")

        elif choice == "2":
            manager.display_employees()

        elif choice == "3":
            employee_id = int(input("Enter Employee ID: "))
            employee = manager.search_employee(employee_id)

            if employee:
                employee.display()
            else:
                print("Employee not found.")

        elif choice == "4":
            employee_id = int(input("Enter Employee ID: "))
            manager.generate_payslip(employee_id)

        elif choice == "5":
            FileManager.save_employees(manager.employees)

        elif choice == "6":
            FileManager.save_employees(manager.employees)
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)