# 2.1
def input_list():
    return list(map(int, input().split(' ')))


my_list = input_list()

# 2.1.1
for i in my_list:
    print(i * 100)

# 2.1.2
print([i * 100 for i in my_list])

# 2.1.3

my = list(map(lambda f: f * 100, my_list))
print(my)

# 2.2.1
list_str = []
for i in my_list:
    list_str.append(str(i))

print(list_str)

#2.2.2
print(2.2)
print([str(i) for i in my_list])

# 2.2.3

st = list(map(str, my_list))
print(st)

# 2.3.3
r = list(map(lambda d: round(d / 100), my_list))
print(r)

# 2.4.3
