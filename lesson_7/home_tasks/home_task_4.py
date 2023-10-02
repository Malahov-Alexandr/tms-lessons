from functools import reduce

text = input('Enter your text: ').split()
split_symbol = input('Enter your split symbol: ')

print(str(reduce(lambda x, y: x + split_symbol+ y, text)))
