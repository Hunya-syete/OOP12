class Course:
    def __init__(self, id, name, code, max_capacity):
        self.id = id
        self.name = name
        self.code = code
        self.max_capacity = max_capacity
        self.trainers = []
        self.enrollments = []
        self.cancelled = False

    def addTrainer(self, trainer):
        self.trainers.append(trainer)

    def addEnrollment(self, enrollment):
        self.enrollments.append(enrollment)

    def isCancelled(self):
        if self.cancelled:
            print(f"The course {self.name} is cancelled.")
        else:
            print(f"The course {self.name} is not cancelled.")
        return self.cancelled