# 1
def hello_world():
    print('Hello World!')


hello_world()
hello_world()
hello_world()


# 2
def my_sum(a, b):
    return a + b


print(my_sum(1, 4))
print(my_sum(75, 34))


# 3

def simple_compare(a, b):
    return a < b


print(simple_compare(1, 4))


# 4
def compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


print(compare(1, 3))
print(compare(3, 2))
print(compare(1, 1))


# 5
def filter_negative_numbers(a):
    new_list = []
    for i in a:
        if i > 0:
            new_list.append(i)
    return new_list


print(filter_negative_numbers([1, 2, 3, 4, -4, -5, -3, -5, 1, 3, 100]))
