from Trainer import Trainer


class Course:
    def __init__(self, identification: str,
                 name: str,
                 code: str,
                 maximum: int,
                 trainers: list[str],
                 enrollments: list
                 ):

        self.identification = identification
        self.name = name
        self.code = code
        self.max = maximum
        self.trainers = trainers
        self.enrollments = enrollments

    def add_trainer(self, trainer: Trainer):
        self.trainers.append(trainer)

    def is_part_time(self):
        return len(self.trainers) > 0


