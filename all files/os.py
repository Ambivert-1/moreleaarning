import os

# Define the path for the directory
directory = 'my_directory'

# Check if the directory does not exist and then create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Now you can list the entries in the directory
entries = os.listdir('my_directory/')
for entry in entries:
    print(entry)
