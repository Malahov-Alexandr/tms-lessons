from person import Person

# 3
list_of_friends = [Person('Alex', 35, 'M'), Person('Ivan', 30, 'M'),
                   Person('Kristina', 28, 'F')]
# 4
for friend in list_of_friends:
    print(friend)


# 5
def get_oldest_person(friends_list: list):
    age = 0
    oldest_friend = None
    for friend in friends_list:
        if friend.age > age:
            age = friend.age
            oldest_friend = friend
    return f'the oldest friend is {oldest_friend}'


# 6
def filter_male_person(friends_list):
    filtered =  list(filter(lambda x: x.gender == 'M', friends_list))
    for friend in filtered:
        print(friend)



result = get_oldest_person(list_of_friends)
print(result)

filter_male_person(list_of_friends)
