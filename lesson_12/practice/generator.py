def generate_squares(count):
    for i in range(1, count + 1):
        a = i ** 2
        yield a
        a += 1


c = 10

test = [i for i in generate_squares(10)]
print(test)
result = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

assert result == test
