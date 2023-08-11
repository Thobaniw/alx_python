import requests
'''
This import requests to be able to access get
'''
import sys
'''
This import sys to be able to pass a commmand line
'''


def send_post_request(url, email):
    """
    Sends a POST request to the provided URL with the email parameter and displays the response body.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to be sent as a parameter.

    Returns:
        None
    """
    try:
        # Prepare the POST request with the email parameter
        data = {'email': email}
        response = requests.post(url, data=data)

        # Display the response body
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    """
    This script takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter,
    and displays the body of the response. It uses the 'requests' and 'sys' packages.
    """
    # Prompt the user to enter the URL and email
    url = input("Enter the URL: ")
    email = input("Enter the email address: ")

    # Call the function to send the POST request and display the response
    send_post_request(url, email)
