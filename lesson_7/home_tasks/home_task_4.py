from functools import reduce

text = input('Enter your text: ').split()
split_symbol = input('Enter your split symbol: ')


def my_join(text, split_symbol):
    return str(reduce(lambda x, y: x + split_symbol + y, text))


print(my_join(text, split_symbol))
