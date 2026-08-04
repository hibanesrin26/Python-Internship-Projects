from person import Person


class Student(Person):

    def __init__(self, student_id, name):
        super().__init__(student_id, name)

    def get_student_id(self):
        return self._person_id

    def display(self):
        print(f"Student ID: {self._person_id}")
        print(f"Student Name: {self._name}")