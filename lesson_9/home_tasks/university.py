from student import Student

students = [Student('Mister Green', 5), Student('Mister Brown', 9),
            Student('Mister Black', 7), Student('Mister White', 8),
            Student('Mister Pink', 6), Student('Mister Up',9)]


def calc_sum_scholarship(students):
    return sum([student.get_scholarship() for student in students])


def get_excellent_student_count(students):
    return len(list(filter(lambda x: x.is_excellent(), students)))


if __name__ == "__main__":
    print(calc_sum_scholarship(students))
    print(get_excellent_student_count(students))
