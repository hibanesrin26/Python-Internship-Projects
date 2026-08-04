import csv
from employee import Employee

class FileManager:

    @staticmethod
    def save_employees(employees, filename="employees.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(["Employee ID", "Employee Name", "Basic Salary"])

                for employee in employees:
                    writer.writerow([
                        employee.get_employee_id(),
                        employee._name,
                        employee.get_basic_salary()
                    ])

            print("Employee data saved successfully.")

        except Exception as e:
            print("Error saving file:", e)

    @staticmethod
    def load_employees(filename="employees.csv"):
        employees = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    employee = Employee(
                        int(row[0]),
                        row[1],
                        float(row[2])
                    )
                    employees.append(employee)

        except FileNotFoundError:
            print("No existing employee data found.")

        except Exception as e:
            print("Error loading file:", e)

        return employees