# User enters a month and gets the numbers of the day in this month

# month : days
month_dict = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30,
              'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}

# User enters a month and get the number of days in this month
print(month_dict[input('Enter a month: ').lower()])

# with a leap year
# a user enter a year and a month and get the number of days in this month
year = int(input('Enter a year: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    month_dict['february'] = 29
print(month_dict[input('Enter a month: ').lower()])
