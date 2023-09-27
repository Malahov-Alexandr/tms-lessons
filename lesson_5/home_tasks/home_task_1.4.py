# the function is accepting a text and returns the longest word


def get_longest_word(text: str) -> str:
    text = text.lower().split(' ')
    biggest_word = ''
    for word in text:
        if len(word) > len(biggest_word):
            biggest_word = word
    return biggest_word


print(get_longest_word('hello this is a string with words and spaces and big big woooooooooord'))
