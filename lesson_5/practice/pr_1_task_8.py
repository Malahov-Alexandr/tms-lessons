# 8
def my_round(number: float, round_to: int = 0):
    if round_to == 0 and number % 1 >= 0.5:
        print('test')
        return int(number) + 1
    elif round_to == 0 and number % 1 < 0.5:
        return int(number)

    else:
        number = str(number)
        index = number.index('.')
        next_digit_after_round_digit = int(number[index+round_to])
        if next_digit_after_round_digit>= 5:
            to_change = int((number)[index+round_to])+1
            return to_change
        else:
            return 'test'


print(my_round(4.123,2))

