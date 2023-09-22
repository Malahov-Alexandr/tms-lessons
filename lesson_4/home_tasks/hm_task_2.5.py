# a user enters the number, needs to count the sum with %, //
user_input = int(input('Enter your number: '))
result = 0

while user_input > 0:  # repeat until there are numbers
    if len(str(user_input)) == 1:       # check if there is only one digit, add it to the result
        result += user_input
        break
    else:
        last_digit = user_input % 10    # get the lat digit
        result += last_digit            # add the last digit to result
        user_input = user_input // 10   # getting a new number without the last digit


print(result)
