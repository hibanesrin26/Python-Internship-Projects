from student import Student

class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                student.display()
                print("-" * 20)

    def search_student(self, student_id):
        for student in self.students:
            if student.get_student_id() == student_id:
                return student
        return None

    def update_marks(self, student_id, new_marks):
        student = self.search_student(student_id)
        if student:
            student.set_marks(new_marks)
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            print("Student deleted successfully.")
        else:
            print("Student not found.")