import subprocess
# Why do we need to finish the task in 5 minutes, if we can automate it and spend 2 hours?


# execute and return the result of execution
def result(command):
    return subprocess.run(command, shell=True, capture_output=True, text=True)


def lazy_execution(command):
    for file in list_of_files:
        # Build the full command by concatenating the stat_command and the file name
        stat_full_command = command + file

        # Write the result to the file
        result_file.write(result(stat_full_command).stdout)


list_of_files = []
stat_command = 'stat '
ls_command = 'ls -l '
result_file = 'auto_file_types.txt'

with open('__text.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        list_of_files.append(line)

with open(result_file, 'w') as result_file:
    lazy_execution(ls_command)
    lazy_execution(stat_command)
