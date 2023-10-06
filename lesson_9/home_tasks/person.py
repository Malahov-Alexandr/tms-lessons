from datetime import datetime


class Person:

    def __init__(self, full_name: str, age: int, gender: str):
        self.full_name = full_name
        self.age = age
        self.gender = self.is_gender(gender)

    def print_person_info(self) -> str:
        return f'Person: {self.full_name} ({self.gender}), {self.age} years old'

    def get_birth_year(self) -> int:
        return datetime.now().year - self.age



    @staticmethod
    def is_gender(gender: str) -> str:
        while True:
            if gender not in ('M', 'F'):
                print('Only accepts M or F')
                gender = input('Please enter your gender (M/F): ')
            else:
                return gender

# the __str__ is just for debug and for information about instance of the class
    def __str__(self):
        return f'{self.full_name}, {self.age}, {self.gender}'

if __name__ == "__main__":
    a = Person('Alexander Malakhau', 35, 'Male')
    print(a.print_person_info())
    print(a.get_birth_year())
