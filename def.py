import sys
import requests
base_url = "http://10.201.21.1"

def logged_in():
    status_response = requests.get(base_url, allow_redirects=False)

    if status_response.status_code == 302:
        redirect_url = status_response.headers['Location']
        if redirect_url==base_url+"/status":
            return True  # Exit the loop if login and status check are successful
        elif redirect_url==base_url+"/login":
            return False
        else:
            final_response = requests.get(redirect_url)
            print("\n\n\nsomething is wrong!\n\n\n")
            print(redirect_url)
            print(final_response.headers)
            sys.exit(1)


def logout():
    logout = requests.get(base_url+'/logout?')
    if not logged_in():
        print("you are logged out, running the script now!\n\n")
    else:
        print("error logging out.")

logout()