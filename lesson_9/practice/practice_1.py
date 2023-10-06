class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = int(age)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def become_older(self):
        self.age += 1
        print(f'Happy birthday, {self.name}!')

        
p = Person('Ivan', 'Ivanov', 20)

# обращение к полям класса
print(p.name)
print(p.surname)
print(p.age)

# вызов метода класса и вывод результата на экран
print(p.get_full_name())

# вызов метода класса + вывод изменившегося поля
p.become_older()
print(p.age)