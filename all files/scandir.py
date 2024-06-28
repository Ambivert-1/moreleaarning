import os

entries = os.scandir('my_directory/')

for entry in entries:
    print(entry.name)
