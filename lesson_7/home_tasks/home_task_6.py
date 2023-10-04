def my_decorator(fucn):
    def wrapper(*args, **kwargs):
        print(f'Функция получила на вход значение {*args, kwargs}')
        result = fucn(*args, **kwargs)
        print(f'Результат функции: {fucn(*args, **kwargs)}')
        return result

    return wrapper


@my_decorator
def my_func(*args, **kwargs):
    return sum([x for x in args]) + sum([x for x in kwargs.values()])


y = my_func(1,2, a=3, b=4)
print(f'y = {y}')
