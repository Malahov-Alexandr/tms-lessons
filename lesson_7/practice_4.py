from functools import reduce


def input_list():
    return list(map(int, input().split(' ')))


my_list = input_list()

# 4.1.3
# s = 0
# su = reduce(lambda x, y: x + y, my_list)
# print(su)


#4.2.3
s = 0
su = reduce(lambda x, y: min(x, y), my_list)
print(su)