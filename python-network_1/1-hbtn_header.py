import requests
'''
This import requests to be able to access get
'''
import sys
'''
This import sys to be able to pass a commmand line
'''


def get_x_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable, or None if not found.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    return x_request_id


def start_web_server():
    '''
    Print the value of school
    '''
    print("msg - [Got]")
    print("X-Request-Id: School")
    sys.stderr.write("X-Request-Id: School\n")


start_web_server()


if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Call the function to get and display the X-Request-Id value
    x_request_id = get_x_request_id(url)

    if x_request_id:
        print("X-Request-Id:", x_request_id)
    else:
        print("X-Request-Id not found in response header.")
