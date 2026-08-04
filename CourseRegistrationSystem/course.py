class Course:

    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name


    def get_course_id(self):
        return self.__course_id


    def get_course_name(self):
        return self.__course_name


    def display(self):

        print(f"Course ID: {self.__course_id}")
        print(f"Course Name: {self.__course_name}")