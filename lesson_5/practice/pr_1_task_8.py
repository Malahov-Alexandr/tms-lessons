# 8
def my_round(number: float, round_to: int = 0):
    # if no number round to, and % > 5 return a simple digit
    if round_to == 0 and number % 1 >= 0.5:
        print('test if "round_to" == 0 and % > 0.5')
        return int(number) + 1
    # if no number round to, and % > 5 return a simple digit
    elif round_to == 0 and number % 1 < 0.5:
        print('test if "round_to" == 0 and % < 0.5')
        return int(number)

    else:
        number = str(number)
        # find the index of '.'
        index = number.index('.')
        # find the next digit after the digit 'round to'
        next_digit_after_round_digit = int(number[index + round_to+1])
        # if digit after round digit > 5 ,'round to' digit+1
        if next_digit_after_round_digit >= 5:
            to_change = int(number[index + round_to])
            # convert sting number without the digit after 'round to' and add changed number
            return float(number[:index+to_change] + str(to_change+1))
        else:
            # convert string number without the digit after 'round to'
            print('test, the last digit less tah 5')
            return float(number[:index+round_to+1])


print(my_round(4.15,1))
