# guess the number from 1 to 100, with hints
import random

random_number = random.randint(1,100)

while True:
    user_input = int(input('Guess the number from 1 to 100: '))
    if user_input > random_number:
        print('не угадал, число меньше загаданного')
        continue
    elif user_input < random_number:
        print('не угадал, число больше загаданного')
        continue
    elif user_input == random_number:
        print('Угадал, молодец')
        break
