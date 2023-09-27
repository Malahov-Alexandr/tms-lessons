# the function return the list of the natural digits **3 from 1 to n

def generate_natural_cubes(n: int = 1) -> list:
    return [i ** 3 for i in range(1, abs(n)+1)]     # abs() is for if there is a negative number (e.g., -5)


# def test_generate_natural_cubes(n):
#     assert generate_natural_cubes(5) == [1, 8, 27, 64, 125]
#     assert generate_natural_cubes(10) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


print(generate_natural_cubes())
