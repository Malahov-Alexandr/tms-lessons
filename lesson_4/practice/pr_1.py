# 1
print(1, sum(i for i in range(0, 101)))

# 2
print(2, sum(i for i in range(100, 1001)))

# 3
print(3, sum(i for i in range(100, 1001) if i % 2 == 0))

# 4
factorial = 1
for i in range(1, 11):
    factorial *= i
print(4, factorial)

# 5
a = 2
for i in range(9):
    a *= 2
print(5, a)

# 6
a = 0
b = 1
while a <= 1000:
    a += b
    b += 1
print(6, a, b - 1)

# issue 2
print(sum(int(i) for i in input('Enter your number: ')))



# issue 4

import random

number = random.randint(1, 15)
while True:
    user_input = int(input("Enter number 1-15: "))
    if number == user_input:
        print('Congratulation')
        break
    else:
        print('Try again')
