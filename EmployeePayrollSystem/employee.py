from person import Person

class Employee(Person):

    def __init__(self, employee_id, name, basic_salary):
        super().__init__(name)
        self.__employee_id = employee_id
        self.__basic_salary = basic_salary

    def get_employee_id(self):
        return self.__employee_id

    def get_basic_salary(self):
        return self.__basic_salary

    def calculate_salary(self):
        hra = self.__basic_salary * 0.20
        da = self.__basic_salary * 0.10
        return self.__basic_salary + hra + da

    def display(self):
        print(f"Employee ID: {self.__employee_id}")
        print(f"Employee Name: {self._name}")
        print(f"Basic Salary: {self.__basic_salary}")
        print(f"Net Salary: {self.calculate_salary()}")