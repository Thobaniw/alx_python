import requests
'''
This import requests to be able to access get
'''
import sys
'''
This import sys to be able to pass a commmand line
'''


def fetch_and_display(url):
    """
    Fetches the content of a URL and displays the response body. Prints an error message if the status code is 400 or higher.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    try:
        response = requests.get(url)

        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    """
    This script takes a URL as input, sends a request to the URL, and displays the body of the response. If the HTTP status
    code is 400 or higher, it prints an error message with the status code. It uses the 'requests' and 'sys' packages.
    """
    url = input("Enter the URL: ")
    fetch_and_display(url)
