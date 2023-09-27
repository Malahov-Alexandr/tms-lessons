# the func takes *args and returns a list of *args elements **2


def generate_squares(*args: int) -> list:
    return [i ** 2 for i in args]


print(generate_squares(1, 2, 3, 4, 5))
