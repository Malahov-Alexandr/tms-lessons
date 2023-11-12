
list_of_files = []
stat_command = 'stat '
ls_command = 'ls -l '
result_file = 'code_lines.txt'
where_to_save = ' >> file_types.txt'

def lazy_execution(command):
    for file in list_of_files:
        # Build the full command by concatenating the stat_command and the file name
        stat_full_command = command + file + where_to_save

        # Write the result to the file
        result_file.write(stat_full_command+'\n')


with open('__text.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        list_of_files.append(line)



with open(result_file, 'w') as result_file:
    lazy_execution(ls_command)
    lazy_execution(stat_command)
