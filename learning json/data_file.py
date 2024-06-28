import json

# Load JSON data from file
with open('data.json', 'r') as read_file:
    data = json.load(read_file)

# Example of using data (printing to console)
print(data)

# Writing data to another file (example)
with open('output.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)
