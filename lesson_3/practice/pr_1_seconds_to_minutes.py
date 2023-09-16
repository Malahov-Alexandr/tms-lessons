# the user enters seconds and in the result gets minutes:seconds
user_input = int(input("Enter seconds: "))

minutes = user_input // 60
seconds = user_input % 60
print(f'{minutes}:{seconds}')


# seconds to days:hours:minutes:seconds
# the number 3600 is a number of seconds in the one hour
days = user_input // (3600 * 24)            # get how many days in the user_input
remaining_second = user_input % (3600 * 24)  # get remaining seconds after counting the days
hours = remaining_second // 3600             # get hours in the remaining seconds
remind_seconds = remaining_second % 3600     # get remaining seconds after counting the hours in the remaining seconds
minutes = remind_seconds // 60              # get minutes in the remaining seconds
seconds = remind_seconds % 60               # get seconds in the remaining seconds
print(f'{days}:{hours}:{minutes}:{seconds}')
