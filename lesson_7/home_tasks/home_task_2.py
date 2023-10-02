vowels = ('a', 'e', 'i', 'o', 'u')

user_input = input().lower().split()
print(list(filter(lambda x: x not in vowels, user_input)))
