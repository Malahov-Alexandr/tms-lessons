# a user enters a three-digit number and gets the sum of it.
number = input('Enter a number: ')
print(int(number[0]) + int(number[1]) + int(number[2]))

# *
print(sum([int(i) for i in number]))
print(sum(map(int, number)))
