user_list = list(range(1, 4))
user_list.append('four')
user_list[1] = 'two'
user_list.append({5, 6, 7})
user_list[-1].add(7)
user_list.insert(2, (2.5,2.6))

print(user_list)
