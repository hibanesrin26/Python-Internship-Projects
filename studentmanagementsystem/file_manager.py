import csv
from student import Student

class FileManager:

    @staticmethod
    def save_students(students, filename="students.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Student ID", "Name", "Age", "Marks"])

                for student in students:
                    writer.writerow([
                        student.get_student_id(),
                        student._name,
                        student._age,
                        student.get_marks()
                    ])

            print("Student data saved successfully.")

        except Exception as e:
            print("Error saving file:", e)

    @staticmethod
    def load_students(filename="students.csv"):
        students = []

        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    student = Student(
                        int(row[0]),
                        row[1],
                        int(row[2]),
                        float(row[3])
                    )
                    students.append(student)

        except FileNotFoundError:
            print("No existing student data found.")

        except Exception as e:
            print("Error loading file:", e)

        return students