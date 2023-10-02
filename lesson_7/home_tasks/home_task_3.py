vowels = ('a', 'e', 'i', 'o', 'u')

user_input = input().split()
print(list(filter(lambda x: x.lower() not in vowels, user_input)))