import json

data = {'name': 'Aleandr', ' sername': 'Malahov', 'age':35}
with open('data.json', 'w') as f:
    json.dump(data, f)
