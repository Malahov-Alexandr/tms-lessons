def my_decorator(fucn):
    def wrapper(x):
        print(f'Функция получила на вход значение {x}')
        print(f'Результат функции: {fucn(x)}')
        result = fucn(x)
        return result

    return wrapper


@my_decorator
def my_func(x):
    return x ** 2


y = my_func(7)
print(f'y = {y}')

a = int(input())
