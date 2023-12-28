import requests

url = ' http://localhost:5000/echo'

# Making a GET request to the Flask route
response = requests.get(url)

# Checking the status code and accessing the JSON content
if response.status_code == 200:
    data = response.json()
    print(data)  # This will print the received JSON content
else:
    print('Request failed with status code:', response.status_code)