# 3.1.3
def input_list():
    return list(map(int, input().split(' ')))


my_list = input_list()

a = list(filter(lambda i: i >= 0, my_list))
print(a)

# 3.2.3
g = list(filter(lambda f: f % 2 != 0, my_list))
print(g)

#3.3.3
m = len(list(filter(lambda b: b > 0, my_list)))
l = len(list(filter(lambda l: l<0, my_list)))
zero = len(list(filter(lambda zero: zero<0, my_list)))
print([m,l,zero])

# do at home 3.4.
