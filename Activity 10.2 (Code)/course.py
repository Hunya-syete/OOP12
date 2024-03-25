class Course:
    def __init__(self, course_id, course):
        self.course_id = course_id
        self.course = course

    def P_Course(self):
        print(f"Id: {self.course_id}\nCourse: {self.course}")
print("\n")
C1 = Course("123456", "BS Computer Engineering")
C1.P_Course()


