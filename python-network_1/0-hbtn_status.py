import requests
'''
import the request to be able to access get
'''


def fetch_and_display_status(url):
    """
    Fetches the status from the given URL and displays the response content.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None
    """
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
    else:
        print("Error:", response.status_code)


# Define the URL you want to fetch
url = "https://alu-intranet.hbtn.io/status"

# Call the function to fetch and display the status
fetch_and_display_status(url)
