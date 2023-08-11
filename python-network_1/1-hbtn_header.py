import requests
'''
This import requests to be able to access get
'''
import sys
'''
This import sys to be able to pass a commmand line
'''


def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from the response header of a given URL.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Extract the value of X-Request-Id from the response headers
        x_request_id = response.headers.get('X-Request-Id')

        # Print message and X-Request-Id
        print("msg - [Got]")
        print("X-Request-Id:", x_request_id)

        # Write X-Request-Id to stderr
        sys.stderr.write("X-Request-Id: School\n")
    except requests.exceptions.RequestException as e:
        # Print an error message if there's a request exception
        print("Error:", e)


if __name__ == "__main__":
    """
    This script takes a URL as input, sends a request to the URL, and displays the value of the X-Request-Id variable
    in the response header. It uses the 'requests' and 'sys' packages.
    """
    # Prompt the user to enter the URL
    url = input("Enter the URL: ")

    # Call the function to fetch and display the X-Request-Id value
    fetch_x_request_id(url)
