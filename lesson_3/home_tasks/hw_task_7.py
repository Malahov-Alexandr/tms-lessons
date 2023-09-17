# return True if a number is simple, else False

number = int(input('Enter your number: '))
result = None

for i in range(2, number):
    if number % i == 0:  # checking that the number is not divided by any number from 1 to number
        result = False
        break  # end the loop if the number is divided by any number from 1 to number
    else:
        result = True

print(result)
