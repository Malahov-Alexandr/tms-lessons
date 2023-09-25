# 1
print(sum([i for i in range(1, 11)]))

# 2

# a = int(input('Enter a number: '))
# b =int(input('Enter a number: '))
# c = int(input('Enter a number: '))
# print(sum([a,b,c]))
# print(max(a,b,c)) #4
# if 0 in [a,b,c]:
#     print('Yes')
# else:
#     print('No')
#

# 5

# l = []
# repeats = int(input('Enter the number of cycles: '))
# for i in range(repeats):
#     text = input('text: ')
#     l.append(text)
# print(l.count('a'))
#
# a = input('new text:' )
# print(a.count('a'))

# 6
# number_1 = int(input())
# number_2 = int(input())
# number_3 = int(input())
# max_dict = 0
# d = dict(a=number_1,b = number_2, c = number_3)
# for key in d:
#     if max_dict < d[key]:
#         max_dict = d[key]
# print(max_dict)

# 7
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
value = 0
max_key = None
d = dict(a=number_1, b=number_2, c=number_3)
for k,v in d.items():
    if value < v:
        value = v
        max_key = k
print(max_key)

