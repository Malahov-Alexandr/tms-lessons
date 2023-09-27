# the function returns  True if the year is leap or False it is not

def is_year_leap(year: int):
    if isinstance(year, int):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return f'the {year} is not the int()'


print(is_year_leap(-2000))
