#!/usr/bin/python3
import requests

# Make a GET request to a URL
response = requests.get("https://intranet.hbtn.io/status")

# Print the status code of the response
print("Status code:", response.status_code)
