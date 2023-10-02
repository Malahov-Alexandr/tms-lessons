user_input = input('Enter your text: ').lower().split()

print(list(map(lambda x: (x.upper(), x.lower()), user_input)))
