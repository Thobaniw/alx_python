import requests
'''
This import requests to be able to access get
'''
import sys
'''
This import sys to be able to pass a commmand line
'''


def search_user_with_letter(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the provided letter as a parameter and displays the result.

    Args:
        letter (str): The letter to be sent as a parameter.

    Returns:
        None
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()

        if json_data:
            user_info = "[{}] {}".format(
                json_data.get('id'), json_data.get('name'))
            print(user_info)
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    """
    This script takes a letter as input and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
    It displays the id and name from the JSON response if properly formatted and not empty.
    """
    letter = input("Enter a letter: ").strip()

    if not letter:
        letter = ""

    search_user_with_letter(letter)
