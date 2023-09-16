# without 'for' loop
x = int(input('Enter number of rubles: '))
y = int(input('Numbers of the years: '))
# 1.1 is 10% of the amount
percents = 1.1 ** y  # count the amount on % for all years
print(round(x * (1.1 ** y), 1))  # multiply the amount on % and round it


# with 'for' loop
for i in range(1, y + 1):  # count of years
    x = x + (x / 100 * 10)  # add 10% of the amount for each year
print(round(x, 1))
