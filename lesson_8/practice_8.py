import csv

with open ('csv_practice_7.csv', 'r') as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        if index == 0:
            print(f'Headers: {row}')
        else:
            print(f'Data: {row}')
        index += 1