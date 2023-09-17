# a user enters a month and numbers of the days if it is in the dict-True, else - False
month_dict = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30,
              'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}

month = input('Enter a month: ').lower()
days = int(input('Input days: '))

# checking the days is more that '0' and lower than amount of days in the month
valid_days = 0 < days <= month_dict[month]
# return True if the month in the dict and the days in the month
print(month in month_dict and valid_days)
