def map_to_tuples(text):
    return list(map(lambda x: (x.upper(), x.lower()), text))


user_input = input('Enter your text: ').lower().split()

print(map_to_tuples(user_input))
