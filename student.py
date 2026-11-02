"""Student record."""


class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.total_classes = 0
        self.attended = 0

    @property
    def percentage(self):
        if self.total_classes == 0:
            return 0.0
        return round(self.attended * 100 / self.total_classes, 2)

    def __repr__(self):
        return (f"Student(roll_no={self.roll_no}, name='{self.name}', "
                f"attendance={self.attended}/{self.total_classes} = {self.percentage}%)")
