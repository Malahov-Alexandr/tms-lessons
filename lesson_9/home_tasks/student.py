class Student:

    def __init__(self, full_name, average_mark):
        self.full_name = full_name
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark < 6:
            money = 60
        elif 6 <= self.average_mark <= 8:
            money = 80
        else:
            money = 100
        return money

    def is_excellent(self):
        return self.average_mark >= 9


if __name__ == "__main__":
    student_1 = Student('Tom Red', 9)
    print(f'Student {student_1.full_name} has {student_1.get_scholarship()} money')
    print(student_1.is_excellent())
