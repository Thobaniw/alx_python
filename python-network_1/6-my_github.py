import requests
'''
This import requests to be able to access get
'''
import sys
'''
This import sys to be able to pass a commmand line
'''


def fetch_github_id(username, password):
    """
    Fetches and displays the GitHub user ID using Basic Authentication with a personal access token.

    Args:
        username (str): Your GitHub username.
        password (str): Your personal access token (password).

    Returns:
        None
    """
    url = "https://api.github.com/user"
    headers = {'Authorization': 'Basic {}:{}'.format(username, password)}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            print(user_info.get('id'))
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    """
    This script takes your GitHub credentials (username and personal access token) as input and uses the GitHub API to display your ID.
    """
    username = input("Enter your GitHub username: ")
    password = input("Enter your personal access token: ")

    fetch_github_id(username, password)
