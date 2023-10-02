import csv

header = ['name', 'surname', 'gender']
data = ['Alexander', 'Malahov', 'M']

with open('csv_practice_6.csv','w') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerow(header)
    writer.writerow(data)
