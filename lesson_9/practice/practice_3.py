class Animal:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def make_voice(self):
        print('Я не знаю какой звук мне издать, я же абстрактное животное')

class Dog(Animal):

    def __init__(self,name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_voice(self):
        print('Гав-гав')


class Cat(Animal):

        def __init__(self,name, age, is_vactinated):
            super().__init__(name, age)
            self.is_vactinated = is_vactinated

        def make_voice(self):
            print('Мяу-мяу')


animals = [
   Animal('Животное', 5), # создание абстрактного животного довольно бессмысленно, но для понимания ООП это ок
   Dog('Шарик', 10, 'Доберман'),
   Cat('Матроскин', 9, True),
]
for animal in animals:
   animal.make_voice()
