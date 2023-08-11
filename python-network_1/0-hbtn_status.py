# Import the `requests` package
import requests

# Define the URL you want to fetch
url = "https://alu-intranet.hbtn.io/status"

# Send a GET request to the URL using the `requests.get()` function
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # If the status code is 200, assume the response content is in JSON format
    # Parse the response content as JSON using the `.json()` method
    data = response.json()

    # Print a header for the response body
    print("Body response:")

    # Display the data type of the response content
    print("\t- type:", type(data))

    # Display the entire content of the response
    print("\t- content:", data)
else:
    # If the status code is not 200, print an error message along with the status code
    print("Error:", response.status_code)
