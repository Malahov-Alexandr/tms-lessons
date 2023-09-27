# the func accepts text and returs the most common word
import random


# a simple solution just returns the most occurs word
# and returns the last word if there are a couple of them
def get_most_frequent_word(text: str) -> str:
    text = text.split(' ')
    count = 0
    common_word = ''
    for word in text:
        word_count = text.count(word)
        if word_count > count:
            count = text.count(word)
            common_word = word
    return common_word

print(get_most_frequent_word('hello this is a string with words and spaces and big big woooooooooord and and and'))


# returns the most occurs word or random word if there are more than one word with the same result
def get_most_frequent_word(text: str):
    list_with_most_occurs_words = []
    word_freq = {}
    words = text.lower().split()
    # add each word to dict if the word in the dict, key value +=1
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    # get the max value
    max_freq_word_value = max(word_freq.values())
    # compare each key value, if keys have the same max value, add it to a list
    for key,value in word_freq.items():
        if word_freq[key] == max_freq_word_value:
            list_with_most_occurs_words.append(key)
    # return max occurs word or return random word from the list
    if len(list_with_most_occurs_words) == 1:
        return list_with_most_occurs_words[0]
    else:
        return random.choice(list_with_most_occurs_words)


print(get_most_frequent_word('hello this is a a a a a string with words and spaces and big big woooooooooord and and and'))
