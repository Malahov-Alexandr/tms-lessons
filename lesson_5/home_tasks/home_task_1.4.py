# the function is accepting a text and returns the longest word
alphabet = 'abcdefghijklmnopqrstuvwxyz '

def get_longest_word(text: str) -> str:
    text = text.lower().split(' ')
    biggest_word = ''
    for word in text:
        for letter in word:
            if letter not in alphabet:
                return 'Invalid input, there are non-alphabetical characters in the text'
            elif len(word) > len(biggest_word):
                biggest_word = word
    return biggest_word


print(get_longest_word('hello0 this is a string with words and spaces and big big woooooooooord'))
