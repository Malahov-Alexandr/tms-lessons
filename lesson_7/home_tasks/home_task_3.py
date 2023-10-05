vowels = ('a', 'e', 'i', 'o', 'u')



def remove_vowels(user_input):
    return list(filter(lambda x: x.lower() not in vowels, user_input))

user_input = input().split()

print(remove_vowels(user_input))
