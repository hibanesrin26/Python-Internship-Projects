from employee import Employee

class PayrollManager:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for employee in self.employees:
                employee.display()
                print("-" * 20)

    def search_employee(self, employee_id):
        for employee in self.employees:
            if employee.get_employee_id() == employee_id:
                return employee
        return None

    def generate_payslip(self, employee_id):
        employee = self.search_employee(employee_id)

        if employee:
            print("\n===== Employee Payslip =====")
            employee.display()
            print("============================")
        else:
            print("Employee not found.")