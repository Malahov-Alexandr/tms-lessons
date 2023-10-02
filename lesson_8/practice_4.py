import json

name = input('Enter your name: ')
sername = input('Enter your sername: ')
age = int(input('Enter your age: '))

data = {'name': name, 'sername': sername, 'age': age}
with open('data_input_practice_4.json', 'w') as f:
    json.dump(data, f)
