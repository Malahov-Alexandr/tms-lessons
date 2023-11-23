import subprocess

list_of_files = []
stat_command = 'stat '
ls_command = 'ls -l '
result_file = 'auto_code_lines.txt'
where_to_save = ' >> file_types.txt'


def result(command):
    return subprocess.run(command, shell=True, capture_output=True, text=True)


def lazy_execution(command):
    for file in list_of_files:
        stat_full_command = command + file

        # Write the result to the file
        result_file.write(result(stat_full_command).stdout)


with open('__text.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        list_of_files.append(line)

with open(result_file, 'w') as result_file:
    lazy_execution(ls_command)
    lazy_execution(stat_command)
