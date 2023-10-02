import csv

name = input('Enter your name: ')
sername = input('Enter your sername: ')
age = int(input('Enter your age: '))

headers = ['name', 'surname', 'age']
data = [name, sername, age]
with open('csv_practice_7.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerow(data)
