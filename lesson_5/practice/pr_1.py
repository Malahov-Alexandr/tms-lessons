# task 1

def hello():
    print('Hello, world!')


hello()


# task 2

def return_hello():
    return 'Hello, world! task 2'


print(return_hello())


# task 3

def hello_name(name):
    print(f'Hello {name}')


hello_name('Alexander')


# task 4
def ret_hello_name(name):
    return f'Hello {name} from task 4'


# task 5
def is_polindrome(text):
    return text == text[::-1]


print(is_polindrome('lol'))


# task 6

def sum_list(numbers: list):
    result = 0
    for i in numbers:
        result += i
    return result


print(sum_list([1, 2, 3, 4, 3, 2, 2]))


# 7
def sum_and_max(*numbers):
    return (f'sum {sum([i for i in numbers])}, max {max(numbers)}')


print(sum_and_max(1, 2, 3, 4, 5, 6, 4, 3, 8, 11))


