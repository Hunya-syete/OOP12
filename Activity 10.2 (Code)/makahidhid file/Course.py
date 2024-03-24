class Course:
    def __init__(self,subject,name,trainer,enrollment,):
        self.subject = subject
        self.name = name
        self.trainer = trainer
        self.enrollment = enrollment

    def printsubject(self):
        print(self.subject,self.name,self,self.trainer,self.enrollment)


