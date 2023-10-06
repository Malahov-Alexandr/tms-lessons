# class User:
#
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password
#
#     def check_password(self, password):
#         return self.__password == password
#
#     def reset_password(self, new_password):
#         self.__password = new_password
#
#
# my_user = User('dima_buevich', 'SuperSecretP@ssword')
#
# # print(my_user.login)
# # # print(my_user.__password)  # так нельзя, будет ошибка
#
# print(my_user.check_password('WrongPassword'))
# print(my_user.check_password('SuperSecretP@ssword'))
#
# my_user.reset_password('NewP@ssword')
#
# print(my_user.check_password('SuperSecretP@ssword'))
# print(my_user.check_password('NewP@ssword'))



class Person:
    count = 0

    def __init__(self, name, count=0):
        self.name = name
        if count:
            Person.count += count
        Person.count += 1

usera = Person('Ivan')
userb = Person('Petr')
userc = Person('Sergey')
print(Person.count)
