import json


with open('data.json', 'r') as read_file:
    data = json.load(read_file)


new_child = {"firstName": "Gita", "age": 4}


data['children'].append(new_child)


print(json.dumps(data, indent=4))


with open('data.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)

