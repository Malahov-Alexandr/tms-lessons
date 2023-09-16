# a user enters a number, as a side of a square and gets the result
# with a tuple where the perimeter of the square, area of the square, diagonal of the square.

side = int(input("Enter a side of a square: "))

perimetr = (side+side) * 2
area = side * 2
diagonal = side * (side ** 0.5)
result = (perimetr, area, round(diagonal, 2))
print(result)
