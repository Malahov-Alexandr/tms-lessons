input_file="code_lines.txt"


# Loop through each line in the file and execute the command
while IFS= read -r command; do
    # Execute the command and append the output to the output file
    eval "$command"
done < "$input_file"