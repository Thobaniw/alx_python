#!/usr/bin/python3
import requests

# Make a GET request to the URL
response = requests.get("https://intranet.hbtn.io/status")

# Print the status code of the response
print("Status code:", response.status_code)

# Print the body response content
print("\nBody response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
