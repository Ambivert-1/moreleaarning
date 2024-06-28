import requests

# Make a GET request to fetch JSON data
response = requests.get("https://jsonplaceholder.typicode.com/todos")

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response directly using response.json()
    todos = response.json()

    # Verify the type of 'todos'
    print(type(todos))  # This will print <class 'list'> because todos is a list of todos

    # Print the first 10 todos
    print(todos[:10])
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
