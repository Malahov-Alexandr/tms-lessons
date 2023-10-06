import datetime
class Person:

    def __init__(self,full_name: str,age: int, gender:str):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        return f'Person: {self.full_name} ({self.gender}), {self.age} years old'

    def get_birth_year(self):
        return datetime - self.age


a = Person('alo',19,'m')
print(a.get_birth_year())