from person import Person

class Student(Person):

    def __init__(self, student_id, name, age, marks):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__marks = marks

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def display(self):
        print(f"ID: {self.__student_id}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Marks: {self.__marks}")