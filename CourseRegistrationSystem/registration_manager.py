class RegistrationManager:

    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []


    def add_student(self, student):
        self.students.append(student)


    def add_course(self, course):
        self.courses.append(course)


    def register_course(self, student_id, course_id):

        self.registrations.append(
            (student_id, course_id)
        )

        print("Course registered successfully.")



    def drop_course(self, student_id, course_id):

        if (student_id, course_id) in self.registrations:

            self.registrations.remove(
                (student_id, course_id)
            )

            print("Course dropped successfully.")

        else:

            print("Registration not found.")



    def display_registrations(self):

        if not self.registrations:

            print("No registrations found.")

        else:

            for reg in self.registrations:

                print(
                    "Student ID:",
                    reg[0],
                    "Course ID:",
                    reg[1]
                )