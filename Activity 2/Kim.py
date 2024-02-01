class Students:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def ave(self):
        self.average = (self.math + self.science + self.english) / 3

    def show(self):
        self.ave()
        print("Name: ", self.name)
        print("Math Grade: ", self.math)
        print("Science Grade: ", self.science)
        print("English Grade: ", self.english)
        if self.math < 75:
            self.status = input("Congratulations! You passed the semester. But you need to re-enroll Math subject. ")
        else:
            if self.science < 75:
                self.status = input("Congratulations! You passed the semester. But you need to re-enroll Science subject.")


        if self.english < 75:
                self.status = input("Congratulations! You passed the semester. But you need to re-enroll English subject.")


        if self.math & self.science & self.english < 75:
               self.status = input("You failed the semester!")

        else: self.status = input("You passed the semester!")

        print("Average Grade: {} ({})".format(round(self.average,0), self.status))

print()
print("Student Average Grade Using Classes in Python")
print()
Name = str(input("Enter Name: "))
Math = float(input("Enter Math: "))
Science = float(input("Enter Science: "))
English = float(input("Enter English: "))
print()

stud = Students(Name, Math, Science, English)
stud.show()
