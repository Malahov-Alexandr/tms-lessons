# #1
# a = int(input())
# b = int(input())
# if a == b:
#     print('Yes')
# else:
#     print('No')
#
# #2
# if a > b:
#     print(a)
# else:
#     print(b)
#
# #3
# if a > 0:
#     print('Positive')
# elif a == 0:
#     print('Negative')
# else:
#     print('negative')
#
#
# #4
# c = int(input())
#
# if a == b == c == 0:
#     print('yes')
# else:
#     print('No')
#

#6
# winter = [12,1,2]
# spring = [3,4,5]
# summer = [6,7,8]
# season = int(input('enter a month: '))
#
# if season in winter:
#     print('Winter')
# elif season in spring:
#     print("Spring")
# elif season in summer:
#     print('Summer')
# else:
#     print('Winter')

#7

# a = int(input())
# b = int(input())
# c = int(input())
# count = 0
# e = [a,b,c]
# for i in e:
#     if i >=0:
#         count+=1
# print(count)

#8
a =int(input())
b=int(input())
c=int(input())
r = None
for number in [a,b,c]:
    if r is None or r < number:
        r = number
print(r)