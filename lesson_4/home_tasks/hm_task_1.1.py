# provide numbers from 5 to 100 (included) that divisible by 5
for i in range(5, 101, 5):
    print(i)

print('-----')

# the same as the above but with 'if' statement
for i in range(5, 101):
    if i % 5 == 0:
        print(i)
