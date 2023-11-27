# Написать тестовый класс TestHomework. В нем реализовать тестовую функцию test_fail_if_john_smith:
# - тест нужно пометить маркером wizard +
# - функция принимает в себя фикстуру age, которое может быть случайным числом от 0 до 100 +
# - до теста нужно выводить фразу Random age is N, где N - сгенерированное случайное число +
# - принимает в себя две параметризированных переменные: first_name, last_name. +
# - first_name может быть John, Harry, Ron, last_name - Smith, Potter, Weasly +
# - функция печатает фразу Hello %first_name% %last_name%! Your age is %age% +
# - если John Smith, то тест xfail +
# - после теста нужно выводить фразу Deleting random age... Done +
# - фикстура age должна быть в файле conftest.py +
# - в файлике pytest.ini нужно прописать параметры, которые показывают более детальную информацию о прогоне и коротки отчет в конце
# - также нужно зарегистрировать маркер +
import pytest


class TestHomework:

    @pytest.mark.parametrize('first_name', ('John', 'Harry', 'Ron'))
    @pytest.mark.parametrize('last_name', ('Smith', 'Potter', 'Weakly'))
    @pytest.mark.wizard
    def test_fail_if_john_smith(self, first_name, last_name, main_fixture, age):
        if first_name == 'John' and last_name == 'Smith':
            pytest.xfail('The full name is John Smith')
        print(f'Hello {first_name} {last_name}! Your age is {age}')
