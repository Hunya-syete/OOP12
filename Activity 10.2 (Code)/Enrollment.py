class Enrollment:
    def __init__(self, student_id, student_name, school_year):
        self.student_id = student_id
        self.student_name = student_name
        self.enrollment_year = school_year

    def P_Enrollment(self):
        print(f"Id: {self.student_id}\nName: {self.student_name}\nYear: {self.enrollment_year}")
print("\n")
Em1 = Enrollment("123456", "Mark", "S.Y 2023-2024")
Em1.P_Enrollment()
