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